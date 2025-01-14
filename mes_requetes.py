
# on va lire tout le contenu de la table d'où l'on veut extraire des données :
# table Vlan de la BDD <modalite>
repVlan = Vlan.objects.using("modalite").raw("SELECT * FROM Vlan")

# ici, on recupère l' id, le numéro du vlan, son nom et le champ divers
# on laisse de côté la date de création et la date de modification
# et on l' écrit dans la BDD <default> de Django
for x in repVlan:
    Vlan.objects.create(id=x.id, num=x.num, nom=x.nom, divers=x.divers).save()

# pareil pour le reste...
repAppareil = Appareil.objects.using("modalite").raw("SELECT * FROM Appareil")
for x in repAppareil:
    Appareil.objects.create(id=x.id, nom=x.nom, divers=x.divers).save()

repMarque = Marque.objects.using("modalite").raw("SELECT * FROM Marque")
for x in repMarque:
    Marque.objects.create(id=x.id, nom=x.nom, divers=x.divers).save()

repAppareiltype = Appareiltype.objects.using("modalite").raw("SELECT * FROM Appareiltype")
for x in repAppareiltype:
    Appareiltype.objects.create(id=x.id, nom=x.nom, divers=x.divers).save()

repEtablissement = Etablissement.objects.using("modalite").raw("SELECT * FROM Etablissement")
for x in repEtablissement:
    Etablissement.objects.create(id=x.id, nom=x.nom, divers=x.divers).save()

repService = Service.objects.using("modalite").raw("SELECT * FROM Service")
for x in repService:
    Service.objects.create(id=x.id, nom=x.nom, divers=x.divers).save()

repNet = Net.objects.using("modalite").raw("SELECT * FROM Net")
for x in repNet:
    Net.objects.create(id=x.id, nom=x.nom, divers=x.divers).save()

repModalite = Modalite.objects.using("modalite").raw("SELECT * FROM Modalite")
for x in repModalite:
    Modalite.objects.create(id=x.id, nom=x.nom, divers=x.divers).save()

repPacs = Pacs.objects.using("modalite").raw("SELECT * FROM Pacs")
for x in repPacs:
    Pacs.objects.create(id=x.id, nom=x.nom, divers=x.divers).save()

repStore = Store.objects.using("modalite").raw("SELECT * FROM Store")
for x in repStore:
    Store.objects.create(id=x.id, nom=x.nom, divers=x.divers).save()

repWorklist = Worklist.objects.using("modalite").raw("SELECT * FROM Worklist")
for x in repWorklist:
    Worklist.objects.create(id=x.id, nom=x.nom, divers=x.divers).save()

repPrinter = Printer.objects.using("modalite").raw("SELECT * FROM Printer")
for x in repPrinter:
    Printer.objects.create(id=x.id, nom=x.nom, divers=x.divers).save()



#-------------------------------------------------------------------------------#

# connexion à la BDD de PROD (modalite) sur la base MySQL du serveur SHOR
# "Index", "Port", "Adresse Ip", "Aet", "Type Machine", "Masque", "Pacs", "Worklist", "Hostname", "Modalite", "Libelle Hote", "Remarque", "Localisation", 
# "Systeme", "Marque", "Appareil", "Store", "MacAdresse", "Vlan", "Dicom", "Inventaire", "DHCP", "Divers", "Fini", "Par", "PingHost", 


repliste = liste_new.objects.using("modalite").raw("SELECT * FROM liste_new")

for x in repliste:
    print(x.aet)