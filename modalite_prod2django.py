import django 
# print("django : ", django)
from django.conf import settings
from modalite import settings as modalite_settings
# print('app_settings.DEBUG : ', modalite_settings.DEBUG)
def get_our_settings():
    return {x: getattr(modalite_settings, x) for x in dir(modalite_settings) if x.isupper()}

if not settings.configured:
    settings.configure(**get_our_settings())
django.setup()

# import pprint
# pprint.pprint(dir(settings))

# from modalite import imagerie
# #settings.configure(default_settings=imagerie_defaults, DEBUG=True)
# settings.configure()
# django.setup()

from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.sessions.models import Session
from imagerie.models import Appareil, Appareiltype, Etablissement, Marque, Modalite, Net, Pacs, Printer, Service, Store, Vlan, Worklist, Localisation
from django.core.cache import cache

from django.contrib.auth import get_user_model
from django.db import transaction
from django.db.models import Avg, Case, Count, F, Max, Min, Prefetch, Q, Sum, When
from django.utils import timezone
from django.urls import reverse
from django.db.models import Exists, OuterRef, Subquery

import mysql.connector

# colonnes de la table <liste_new> dans la BDD de production (MySQL):   
#         0       1       2          3            4          5         6         7          8          9      10       11         12        13         14
col = ['Index','Ping','Telnet','Ping Echo','Echo Modalite','Port','Adresse Ip','Aet','Type Machine','Masque''Pacs','EchoStore','Routage','Worklist','Hostname', 
'Modalite','Libelle Hote','Remarque','Localisation','Systeme','Marque','Appareil','Store','EchoWorklist','MacAdresse','Vlan','Dicom','Inventaire','DHCP','PingHost']
#   15           16           17           18          19        20        21        22          23           24        25      26        27        28       29

config = {
    "host": "127.0.0.1",
    "user": "kligliro",
    "password": "%LokO80%",
    "database": "modalite",
}

def maj_vlan(liste_net):
    vlan = Vlan.objects.all()
    dic_vlan = {}
    for z in vlan:                   # on crée un dictionnaire des vlans existants..
        dic_vlan[str(z.num)]=z.id    # avec le n° de vlan comme clé et son index comme valeur
    len_dic_vlan = len(dic_vlan)     # on stocke la taille de <dic_vlan> dans <lendic_vlan>
    print('-----> dic_vlan.keys = ', dic_vlan.keys())
    print('taille de dic_vlan : ', len_dic_vlan)
    set_dic_vlan = set(dic_vlan)
    print()
    print('set_dic_vlan = ', set_dic_vlan)
    print('taille de set_dic_vlan  : ', len(set_dic_vlan ))
    # recherche de nouveaux vlan dans liste_new
    dic_vlan_new = {}
    liste_vlan_new = []
    # liste_net = [(row[6], row[14], row[24], row[9], "", "", "", dhcp, row[25]), ..... ]
    for x in liste_net:
        liste_vlan_new.append(x[8])
    #print()
    #print('liste_vlan_new = ', liste_vlan_new)
    #print('taille de liste_vlan_new  : ', len(liste_vlan_new ))

    set_vlan_new = set(liste_vlan_new)
    print()
    print('set_vlan_new = ', set_vlan_new)
    print('taille de set_vlan_new  : ', len(set_vlan_new ))
    print()
    print('set_vlan_new | set_dic_vlan : ', set_vlan_new | set_dic_vlan, '   taille : ', len(set_vlan_new | set_dic_vlan)) 
    print()
    print('set_vlan_new & set_dic_vlan : ', set_vlan_new & set_dic_vlan, '   taille : ', len(set_vlan_new & set_dic_vlan))

    for num_vlan in set_vlan_new|set_dic_vlan:
        if num_vlan not in set_dic_vlan:
            if num_vlan == '':
                pass
            else:
                print(f"le vlan {num_vlan} n'existe pas, on va le créer")
                Vlan.objects.create(num=num_vlan).save()
        else:
            print(f"le vlan {num_vlan} existe déjà")

def maj_Net(liste_net):
    vlan = Vlan.objects.all()
    dic_vlan = {}
    for z in vlan:                   # on crée un dictionnaire des vlans existants..
        dic_vlan[str(z.num)]=z.id 
    cpt = 0
    for x in liste_net:
        cpt += 1
        if x[8] == '':
            id_vlan = ''
        else:
            id_vlan = dic_vlan[x[8]]

        print(f"'addrip='{x[0]}, 'hostname='{x[1]} , 'macaddr='{x[2]}, 'masq='{x[3]}, 'gw='{x[4]}, 'dns1='{x[5]}, 'dns2='{x[6]}, 'dhcp='{x[7]}, 'vlan_id='{id_vlan}")
        Net.objects.create(addrip=x[0] , hostname=x[1] , macaddr=x[2] , masq=x[3] , gw=x[4] , dns1=x[5] , dns2=x[6] , dhcp=x[7] , vlan_id=id_vlan).save()
    print('cpt : ', cpt)


def maj_Localisation(liste_localisation):
    cpt = 0
    for x in liste_localisation:
        cpt += 1
        Localisation.objects.create(code=x).save()
    print('cpt : ', cpt)

def maj_Worklist(liste_worklist):
    cpt = 0
    for x in liste_worklist:
        print(x)
        cpt += 1
        Worklist.objects.create(nom=x[1], aet=x[2], port=x[4]).save()
        #['id', 'net', 'nom', 'aet', 'port'] 
    print('cpt : ', cpt)


def maj_Appareil(liste_net):
    liste_appareil_net = []
    cpt = 0
    for x in liste_net:
        cpt += 1
        liste_appareil_net.append(x[21])
    set_liste_appareil_net = set(liste_appareil_net)
    print(set_liste_appareil_net, "   ", len(set_liste_appareil_net))
    print('cpt : ', cpt)

def maj_Modalite(liste_net):
    cpt = 0
    liste_appareil_net = []

    for x in liste_net:
        cpt += 1
        liste_appareil_net.append(x[21])
    set_liste_appareil_net = set(liste_appareil_net)
    #print("set_liste_appareil_net : ", set_liste_appareil_net, "   taille : ", len(set_liste_appareil_net))
    
    dic_appareil = {}
    for id, nom in enumerate(set_liste_appareil_net, 1): 
        #if nom == '':
        #    continue         
        dic_appareil[nom]=id 
    #print("dic_appareil : ", dic_appareil, "  taille : ", dic_appareil)
    cpt = 0
    for x in liste_net:
        if x != "":
            #print(x)
            cpt += 1
            #print("x.Appareil = ", x[21])  
            #print("appareil = x[21] = ", x[21])  
            try :
                appareil = Appareil.objects.raw(f"select id from Appareil where nom = '{x[21]}' ")[0]
                appareil_id = appareil.id
            except:
                appareil_id = ''
                #print("!!! appareil = ", x[21]) 
            #appareil = Appareil.objects.raw(f"SELECT * FROM Appareil WHERE nom='Serveur' ")
            #appareil = Appareil.objects.all()
            ##appareil = dic_appareil[x[21]]
            ##appareiltype = dic_appareil[x[8]]
            #print("appareiltype = x[8] = ", x[8])  
            try:
                appareiltype = Appareiltype.objects.raw(f"select id from Appareiltype where nom = '{x[8]}' ")[0]
                appareiltype_id = appareiltype.id
            except:
                appareiltype_id = ''
                #print("!!! appareiltype = ", x[8])

            aet = x[7]

            port = x[5]
            ##pacs = dic_appareil[x[10]]
            #print("pacs = x[10] = ", x[10])
            try:
                pacs = Pacs.objects.raw(f"select id from Pacs where aet = '{x[10]}' ")[0]
                pacs_id = pacs.id
            except:
                pacs_id = ''
                #print("!!! pacs = ", x[8])  
            
            ##service = dic_appareil[x[18]]
            #print("loc = x[18] = ", x[18]) 
            try:
                loc = Localisation.objects.raw(f"select id from Localisation where code = '{x[18]}' ")[0]
                loc_id = loc.id
            except:
                loc_id = ''
                #print("!!! loc = ", x[18])  
            
            ##worklist = dic_appareil[x[13]]
            #print("worklist = x[13] = ", x[13])  
            try:
                worklist = Worklist.objects.raw(f"select id from worklist where aet = '{x[13]}' ")[0]
                worklist_id = worklist.id
            except:
                worklist_id = ''
                #print("!!! worklist= ", x[13])  
            
            ##net = dic_appareil[x[6]]
            #print("net = x[6] = ", x[6])  
            try:
                net = Net.objects.raw(f"select id from Net where addrip = '{x[6]}' ")[0]
                net_id = net.id
            except:
                net_id = ''
                #print("!!! net= ", x[6])  

            #print("---------->", type(appareil_id)," . ", type(appareiltype_id)," . ", type(aet)," . ", type(port)," . ", type(pacs_id)," . ", type(loc_id)," . ", type(worklist_id)," . ", type(net_id))
            #print("---------->", appareil_id," . ", appareiltype_id," . ", aet," . ", port," . ", pacs_id," . ", loc_id," . ", worklist_id," . ", net_id)
            Modalite.objects.create(appareil_id=appareil_id, appareiltype_id=appareiltype_id, aet=aet, port=port, pacs_id=pacs_id , loc_id=loc_id , worklist_id=worklist_id, net_id=net_id).save()
            #list_col_Modalite = ['id', 'appareil', 'appareiltype', 'aet', 'port', 'pacs', 'service', 'worklist', 'net', 'store', 'printer']
            #print(f"{appareil}, {appareiltype}, {aet}, {port}, {pacs}, {service}, {worklist}, {net}")
            #
            #print('---')
            #print(appareil, appareil[0])
    print('cpt : ', cpt)

#         0       1       2          3            4          5         6         7          8          9      10       11         12        13         14
col = ['Index','Ping','Telnet','Ping Echo','Echo Modalite','Port','Adresse Ip','Aet','Type Machine','Masque''Pacs','EchoStore','Routage','Worklist','Hostname', 
'Modalite','Libelle Ho  te','Remarque','Localisation','Systeme','Marque','Appareil','Store','EchoWorklist','MacAdresse','Vlan','Dicom','Inventaire','DHCP','PingHost']
#   15           16           17           18          19        20        21        22          23           24        25      26        27        28       29

cnx = mysql.connector.connect(**config)

# cnx = connect_to_mysql(config, attempts=3)
if cnx and cnx.is_connected():
    with cnx.cursor() as cursor:
        liste_net = []
        result = cursor.execute("SELECT * FROM liste_new")
        rows = cursor.fetchall()
        for row in rows:
            #print(row)
            liste_net.append(row)

        #set_net = set(liste_net)         # au cas où il y aurait la même ligne qqpart !
        #maj_vlan(liste_net)
        #maj_Net(liste_net)
        #maj_Localisation(liste_localisation)
        #maj_Worklist(liste_worklist)
        #maj_Appareil(liste_net)
        maj_Modalite(liste_net)
        
    cnx.close()

else:
    print("Could not connect")


# colonnes de la table <liste_new> dans la BDD de production (MySQL):   
#         0       1       2          3            4          5         6         7          8          9      10       11         12        13         14
col = ['Index','Ping','Telnet','Ping Echo','Echo Modalite','Port','Adresse Ip','Aet','Type Machine','Masque''Pacs','EchoStore','Routage','Worklist','Hostname', 
'Modalite','Libelle Hote','Remarque','Localisation','Systeme','Marque','Appareil','Store','EchoWorklist','MacAdresse','Vlan','Dicom','Inventaire','DHCP','PingHost']
#   15           16           17           18          19        20        21        22          23           24        25      26        27        28       29

# colonnes de la table <Net> dans la BDD de repos_modalite (SQLITE django): 
list_col_Net =['id', 'addrip', 'hostname', 'macaddr', 'masq', 'gw', 'dns1', 'dns2', 'dhcp', 'vlan_id']   # fait

# colonnes de la table <Modalite> dans la BDD de repos_modalite (SQLITE django) : 
list_col_Modalite = ['id', 'aet', 'nom', 'net', 'port', 'pacs', 'worklist', 'store', 'printer', 'service']

list_col_Appareil = ['id', 'nom', 'divers']              # fait
list_col_Localisation = ['id', 'code', 'nom']            # fait
list_col_Marque = ['id', 'nom', 'divers']                # fait
list_col_Appareiltype = ['id', 'nom', 'divers']          # fait
list_col_Vlan = ['id', 'num', 'nom', 'divers']           # fait
list_col_Etablissement = ['id', 'nom', 'divers']         # fait
list_col_Service = ['id', 'nom', 'divers']               # fait
list_col_Pacs = ['id', 'net', 'nom', 'aet', 'port']      # fait
list_col_Store = ['id', 'net', 'nom', 'aet', 'port']     # fait
list_col_Worklist = ['id', 'net', 'nom', 'aet', 'port']  # fait
list_col_Printer = ['id', 'net', 'nom', 'aet', 'port']   # fait



# liste_localisation.append(rows[18])
# print(liste_localisation)
# print(len(liste_localisation))
# print("----------------------------------------------------------------------------------")
# set_localisation = set(liste_localisation)
# print(set_localisation)
# print(len(set_localisation
# liste_worklist.append(rows[13])
# print(liste_worklist)
# set_worklist = set(liste_worklist)
# print(set_worklist)
# print(liste_net)
# print(len(liste_net))
# print("----------------------------------------------------------------------------------"
# print(set_net)
# print(len(set_net
# liste_pacs.append(rows[10])
# set_pacs = set(liste_pacs)
# print(set_pacs)
# for sp in set_pacs:


