from django.core.management.base import BaseCommand
from imagerie.models import Modalite
from django.utils import timezone
from django.db.models import Q
from pathlib import Path
from modalite.settings import BASE_DIR
import csv

fic_csv = str(BASE_DIR) + "/private/recup_imagerie_last/liste_new_202510031116_imagerie.csv"
       
class Command(BaseCommand):
    args = ''
    help = "intégration des colonnes 'inventaire' et 'n° de système' dans la BDD à partir de de l'ancien 'imagerie'"

    def handle(self, *args, **options):
        contenu = "intégration des colonnes 'inventaire' et 'n° de système' dans la BDD à partir de de l'ancien 'imagerie'\n"
        with open('inv_system.txt', 'a') as f:
            f.write(contenu)
            # modalites = Modalite.objects.all()        
            count = 0  
            countpb = 0
            col_csv = ['Index', 'Ping', 'Telnet', 'Ping Echo', 'Echo Modalite', 'Port',	'Adresse Ip', 'Aet', 'Type Machine', 'Masque', \
                #         0        1        2          3             4             5          6         7          8            9  
                'Pacs', 'EchoStore',	'Routage', 'Worklist', 'Hostname', 'Modalite', 'Libelle Hote', 'Remarque', 'Localisation', \
                # 10         11             12          13         14          15             16            17            18
                'Systeme', 'Marque', 'Appareil', 'Store', 'EchoWorklist', 'MacAdresse', 'Vlan', 'Dicom', 'Inventaire', 'DHCP', 'PingHost']
                #   19        20         21         22          23              24        25       26         27         28        29
    
            with open(fic_csv, newline='') as csvfile:
                modalite = csv.reader(csvfile, delimiter=',', quotechar='"')
                next(modalite)       # on passe la première ligne
                # on sélectionne les colonnes sur lesquelles on veut matcher les modalités (AET, addrip, macaddr)
                # et celles que l' on veut récupérer (systeme, inventaire, remarque).
                # j' ai viré du fichier csv les lignes ayant une adresse IP en 0.0.0.0 qui posent soucis.
                for row in modalite:
                    # (modalite)    aet           addrip           macaddr           n_system         n_invent         commentaire
                    # (imagerie)    AET         Adresse Ip'      MacAdresse          systeme         inventaire         remarque
                    try:
                        #print(f'--> id: {row[0]:<5} aet: {row[7]:<26} addrip: {row[6]:<16} macaddr: {row[24]:<18} systeme: {row[19]:<25} inventaire: {row[27]:<25} ')
                        f.write(f'--> id: {row[0]:<5} aet: {row[7]:<26} addrip: {row[6]:<16} macaddr: {row[24]:<18} systeme: {row[19]:<25} inventaire: {row[27]:<25}\n')
                        modal = Modalite.objects.filter(addrip=row[6])   #  , macaddr=row[24], aet=row[7]
                        for m in modal:
                            print(f'<-- id: {m.id:<5} aet: {m.aet} {" " * 18} addrip: {m.addrip:<16} macaddr: {m.macaddr} systeme: {m.n_system} \
                                inventaire: {m.n_invent} comment: {m.commentaire}')
                            f.write(f'<-- id: {m.id:<5} aet: {m.aet} {" " * 18} addrip: {m.addrip:<16} macaddr: {m.macaddr} systeme: {m.n_system} \
                                inventaire: {m.n_invent} comment: {m.commentaire}\n')
                            if row[19] and not m.n_system:
                                m.n_system = row[19]
                                print(f"ajout du n° de système : {row[19]} pour ma modalité avec l' ID : {m.id} \n")
                                f.write(f'ajout du n° de système : {row[19]}\n')
                            if row[27] and not m.n_invent:
                                m.n_invent = row[27]
                                print(f"ajout du n° d'inventaire : {row[27]} pour ma modalité avec l' ID : {m.id} \n")
                                f.write(f"ajout du n° d'inventaire : {row[27]}\n")
                            if row[17] and not m.commentaire:
                                m.commentaire = row[17]
                                print(f"ajout du commentaire : {row[17]} pour ma modalité avec l' ID : {m.id} \n")
                                f.write(f'ajout du commentaire : {row[17]}\n')                            
                        m.save()     
                        count += 1                  
                    except:
                        print(f'!!! id:  {row[0]:<5}  addrip:  {row[6]:<16} macaddr:  {row[24]:<18}   il y a problème avec cette modalié.')
                        f.write(f'!!! id:  {row[0]:<5}  addrip:  {row[6]:<16} macaddr:  {row[24]:<18}   il y a problème avec cette modalié.\n')
                        count += 1
                        countpb += 1
                OK = f"nombre de lignes examinées : {count}"
                KO = f"nombre de lignes avec pbs  : {countpb}"
                print(OK)
                print(KO)
                f.write(OK + "\n")
                f.write(KO + "\n")    
    
