from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from django.db import models
from django.db.models import UniqueConstraint
from datetime import timedelta
from django.utils import timezone
from django.utils.html import format_html
from simple_history.models import HistoricalRecords

# class MUser(AbstractUser):
#     is_premium = models.BooleanField(default=False)
#     good_reputation = models.BooleanField(default=False)

class Appareil(models.Model):
    nom = models.CharField(max_length=45, blank=True, null=True)
    divers = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Appareil'
        ordering = ['nom']

    def __str__(self):
        return "{0}".format(self.nom)

class Localisation(models.Model):
    code = models.CharField(blank=True, null=True, max_length=30) 
    nom = models.CharField(blank=True, null=True, max_length=30)  
    # nomutil = models.CharField(blank=True, null=True, max_length=30) 
    # tel = models.CharField(blank=True, null=True, max_length=30) 
    # divers = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Localisation'
        ordering = ['code']

    def __str__(self):
        return "{0}".format(self.code)

class Marque(models.Model):
    nom = models.CharField(max_length=30, blank=True, null=True)
    divers = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Marque'
        ordering = ['nom']

    def __str__(self):
        return "{0}".format(self.nom)

class Appareiltype(models.Model):
    nom = models.CharField(max_length=45, blank=True, null=True)
    divers = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'AppareilType'
        ordering = ['nom']

    def __str__(self):
        return "{0}".format(self.nom)    


class Vlan(models.Model):
    num = models.IntegerField(unique=True, blank=True, null=True)
    nom = models.CharField(max_length=45, blank=True, null=True)
    divers = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Vlan'
        ordering = ['nom']

    def __str__(self):
        #return "{0} {1}".format(self.nom, self.num, self.divers)
        return "{0} -> {1}".format(self.num, self.nom)

class Etablissement(models.Model):
    nom = models.CharField(max_length=45, blank=True, null=True)
    # site = models.CharField(max_length=45, blank=True, null=True)
    divers = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Etablissement'

    def __str__(self):
        return "{0}".format(self.nom)

class Service(models.Model):
    nom = models.CharField(max_length=45, blank=True, null=True)
    divers = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Service'
        ordering = ['nom']

    def __str__(self):
        return "{0}".format(self.nom)
     
  
    
class Identifiant(models.Model):
    login = models.CharField(blank=True, null=True, max_length=128) 
    #password = models.CharField(blank=True, null=True, max_length=30, default="voir TeamPass") 
    divers = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Identifiant'

    def __str__(self):
        return "{0}".format(self.login)   
       



class Contact(models.Model):
    societe =  models.CharField(blank=True, null=True, max_length=128) 
    nom = models.CharField(blank=True, null=True, max_length=30) 
    prenom = models.CharField(max_length=30, blank=True, null=True)
    mail = models.EmailField(max_length=50, blank=True, null=True)
    telmobile = models.CharField(max_length=30, blank=True, null=True)
    telfixe = models.CharField(max_length=30, blank=True, null=True)
    dect = models.CharField(max_length=30, blank=True, null=True)
    divers = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Contact'

    def __str__(self):
        return "{0} {1}".format(self.nom, self.prenom)


class Ras(models.Model):
    denom = models.CharField(blank=True, null=True, max_length=128) 
    contact = models.ForeignKey('Contact', null=True, blank=True, on_delete=models.PROTECT, related_name='ras_contact', help_text=_(" Contact "), )
    divers = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Ras'

    def __str__(self):
        return "{0} ".format(self.denom) 


class Resspartage(models.Model):
    nom = models.CharField(blank=True, null=True, max_length=128) 
    chemin = models.CharField(blank=True, null=True, max_length=255) 
    # projet = models.ForeignKey('Projet', null=True, blank=True, on_delete=models.PROTECT, related_name='resspartage_projet', help_text=_(" Projet "), ) 
    identifiant = models.ManyToManyField('Identifiant', blank=True, help_text=_(" Identifiant # "), ) 
    # password = models.CharField(blank=True, null=True, max_length=30, default="voir TeamPass") 
    divers = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Resspartage'

    def __str__(self):
        return "{0} ".format(self.chemin)  


class Bdd(models.Model):
    nom = models.CharField(blank=True, null=True, max_length=128) 
    unc = models.CharField(blank=True, null=True, max_length=255)
    host = models.CharField(blank=True, null=True, max_length=30) 
    port = models.IntegerField(blank=True, null=True, help_text=_(" Port BDD ")) 
    # projet = models.ForeignKey('Projet', null=True, blank=True, on_delete=models.PROTECT, related_name='bdd_projet', help_text=_(" Projet "), ) 
    identifiant = models.ManyToManyField('Identifiant', blank=True, help_text=_(" Identifiant # "), )  
    # password = models.CharField(blank=True, null=True, max_length=30) 
    divers = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Bdd'

    def __str__(self):
        return "{0} ".format(self.nom)   


class Connection(models.Model):
    nom = models.CharField(blank=True, null=True, max_length=128) 
    ras = models.ForeignKey('Ras', null=True, blank=True, on_delete=models.PROTECT, related_name='Connection_ras', help_text=_(" compte ras_xxx "), )
    resspartage = models.ForeignKey('Resspartage', null=True, blank=True, on_delete=models.PROTECT, related_name='Connection_resspartage', help_text=_(" ressource partagée "), )
    bdd = models.ForeignKey('Bdd', null=True, blank=True, on_delete=models.PROTECT, related_name='Connection_bdd', help_text=_(" connexion à BDD "), )
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Connection'

    def __str__(self):
        return "{0} ".format(self.nom)  
    
    
class Soft(models.Model):
    
    def one_year_from_today():
        return timezone.now() + timedelta(days=365)

    SOFTTYPES = [
        ("NA", "N/A"),                       # serveur Non Applicable
        ("OS", "Sysyteme d'exploitation"),   # Windows, Linux, Mac... et leur version  
        ("APP", "Logiciel métier"),          # serveur PHYSIQUE
    ]
    demande = models.CharField(blank=True, null=True, max_length=30)    # n° de demande dans GEQIP  ex: DEM-2024-02347
    softtype = models.CharField(max_length=3, null=True, blank=True, choices=SOFTTYPES, default="VM")   #  type de logiciel
    nom = models.CharField(blank=True, null=True, max_length=30) 
    version = models.CharField(max_length=30, blank=True, null=True)
    licence= models.CharField(blank=True, null=True, max_length=255, help_text=_("max d' info sur celle-ci (n°, clé USB, dongle, flottante,.... ?"))
    validité = models.DateTimeField(default=one_year_from_today, verbose_name='valide jusque...')
    fournisseur= models.CharField(blank=True, null=True, max_length=30)  
    
    # projet = models.ForeignKey('Projet', null=True, blank=True, on_delete=models.PROTECT, related_name='soft_projet', help_text=_(" Projet "), ) 
    #referent = models.CharField(max_length=30, blank=True, null=True)
    # marche = models.CharField(max_length=30, blank=True, null=True)
    divers = models.CharField(max_length=255, blank=True, null=True)
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Logiciel'

    def __str__(self):
        return "{0} {1} ".format(self.nom, self.version)


class Hard(models.Model):
    STYPES = [
        ("NA", 'N/A'),          # serveur Non Applicable
        ("VM", 'VM'),         # serveur VIRTUEL
        ("PHY", 'PHYSIQUE'),    # serveur PHYSIQUE
    ]
    editeur = models.CharField(max_length=30, blank=True, null=True) 
    description = models.CharField(max_length=250, blank=True, null=True) 
    #alias = models.CharField(max_length=30, blank=True, null=True) 
    stype = models.CharField(max_length=3, null=True, blank=True, choices=STYPES, default="VM")   #  serveur type
    ram = models.CharField(max_length=10, blank=True, null=True)
    core = models.IntegerField(blank=True, null=True) 
    ddsystem = models.CharField(max_length=10, blank=True, null=True) 
    dddata = models.CharField(max_length=10, blank=True, null=True)  
    #projet = models.ForeignKey('Projet', null=True, blank=True, on_delete=models.PROTECT, related_name='ordi_projet', help_text=_(" Projet "), )        
    doc = models.FileField(blank=True, null=True, upload_to="documentations")
    divers = models.CharField(max_length=1024, blank=True, null=True) 
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Hard'
        ordering = ["description"]

    def __str__(self):
        return "{0}".format(self.description)


class Projet(models.Model):
    nom = models.CharField(blank=True, null=True, max_length=128) 
    demande = models.CharField(blank=True, null=True, max_length=50)
    contact = models.ForeignKey('Contact', null=True, blank=True, on_delete=models.PROTECT, related_name='projet_contact', help_text=_(" Contact "), )
    service = models.ForeignKey('Service', null=True, blank=True, on_delete=models.PROTECT, related_name='projet_service', help_text=_(" Service "), )  
    editeur = models.CharField(max_length=50, blank=True, null=True)
    softs = models.ManyToManyField('Soft', blank=True, related_name='projet_softs', help_text=_(" Logiciels achetés, fournis..."), )  
    hards = models.ManyToManyField('Hard', blank=True, related_name='projet_hards', help_text=_(" matériels achetés, fournis... "), ) 
    divers = models.CharField(max_length=255, blank=True, null=True)
    doc = models.FileField(blank=True, null=True, upload_to="documentations")
    datecreat = models.DateTimeField(auto_now_add=True, verbose_name='date de création')
    datemodif = models.DateTimeField(auto_now_add=True, verbose_name='date de modification')
    datefin = models.DateTimeField(auto_now_add=True, verbose_name='date de finalisation')
    history = HistoricalRecords()
    
    class Meta:
        managed = True
        db_table = 'Projet'

    def __str__(self):
        return "{0}".format(self.nom)


class Modalite(models.Model): 
    SERVEURS = [
        ("NA", 'N/A'),      # serveur Non Applicable
        ("PA", 'PACS'),     # serveur DICOM PACS
        ("WL", 'WL'),       # serveur DICOM WORKLIST
        ("DA", 'DACS'),     # serveur de dose DICOM 
        ("ST", 'STORE'),    # serveur DICOM STORE
        ("PR", 'PRINT'),    # serveur DICOM PRINT pour l' impression        
        ("IN", 'INFORM'),   # serveur informatique virtuel ou physique
        ("UC", 'ORDI'),     # ordinateur
        ("OT", 'OTHER'),    # autre catégorie...
    ]
    
    # nom      = models.CharField(max_length=30, blank=True, null=True) 
    appareil = models.ForeignKey('Appareil', null=True, blank=True, on_delete=models.PROTECT, related_name='modalite_appareil',help_text=_(" Appareil ") )
    appareiltype = models.ForeignKey('AppareilType', null=True, blank=True, on_delete=models.PROTECT, related_name='modalite_appareiltype',help_text=_(" Appareiltype ") )
    # alias    = models.CharField(max_length=30, blank=True, null=True)   
    serveur  = models.CharField(max_length=2, null=True, blank=True, choices=SERVEURS, default="NA") 
    hard = models.OneToOneField('Hard', null=True, blank=True, on_delete=models.PROTECT, related_name='modalite_hard', help_text=_(" configuration matérielle de la machine "))
    soft = models.ManyToManyField('Soft', blank=True, related_name='modalite_soft', help_text=_(" configuration logicielle de la machine "))
    Connection = models.OneToOneField('Connection', null=True, blank=True, on_delete=models.PROTECT, related_name='modalite_Connection', help_text=_(" connnectivité de la machine "))
    addrip = models.GenericIPAddressField(default="0.0.0.0", blank=True, null=True)
    hostname = models.CharField(max_length=30, blank=True, null=True) 
    commentaire = models.CharField(max_length=255, blank=True, null=True)
    macaddr = models.CharField(max_length=20, blank=True, null=True) 
    vlan = models.ForeignKey('Vlan', null=True, blank=True, on_delete=models.PROTECT, related_name='net_vlan', help_text=_(" Vlan "), ) 
    mask = models.CharField(max_length=20, blank=True, null=True, default='255.255.255.0')
    gw = models.GenericIPAddressField(default="0.0.0.1", blank=True, null=True)
    dns1 = models.GenericIPAddressField(default="10.200.1.10", blank=True, null=True)
    dns2 = models.GenericIPAddressField(default="172.25.16.10", blank=True, null=True)
    dhcp = models.BooleanField(default=False)
    aet      = models.CharField(max_length=30, blank=True, null=True, help_text=_(" Aet ")) 
    port     = models.IntegerField(blank=True, null=True, help_text=_(" Port DICOM ")) 
    # divers   = models.CharField(max_length=1024, blank=True, null=True) 
    # modedegrade =  models.TextField(blank=True, null=True, help_text=_(" mode dégradé à mettre en place.. "))
    # doc      = models.FileField(blank=True, null=True, upload_to="documentations")
    pacs     = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT, related_name='modalite_pacs',help_text=_(" Pacs ") )  
    worklist = models.ForeignKey('self', null=True, blank=True, on_delete=models.PROTECT, related_name='modalite_worklist',help_text=_(" Worklist ") )
    stores    = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='modalite_stores', help_text=_(" différents STORE où l'on peut pousser les examens"))
    printers  = models.ManyToManyField('self', blank=True, symmetrical=False, related_name='modalite_printers', help_text=_(" différents PRINT où l'on peut imprimer les examens"))
    # modalite = models.CharField(max_length=5, blank=True, null=True, help_text=_(" CT, CR, DX, US, MR, etc... ")) 
    service  = models.ForeignKey('Service', null=True, blank=True, on_delete=models.PROTECT, related_name='modalite_service', help_text=_(" Service ") )
    loc = models.ForeignKey('Localisation', null=True, blank=True, on_delete=models.PROTECT, related_name='modalite_loc',help_text=_(" Localisation ") )
    reforme = models.BooleanField(default=False, help_text=(" réformé ? "))
    ping = models.BooleanField(default=False, help_text=(" joignable par ping ? "))
    recent_ping = models.DateTimeField(null=True, blank=True)
    first_ping = models.DateTimeField(null=True, blank=True)
    history = HistoricalRecords()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['addrip', 'aet', 'port'], name='unique_dicom') # trio DICOM !
        ]
        managed = True
        db_table = 'Modalite'
        ordering = ["aet"]

    def __str__(self):
        return "{0}".format(self.aet)

    def colored_addrip(self):
        # url ='/admin/imagerie/modalite/{}/change/'.format(self.id)
        url ='/{}/'.format(self.addrip)
        if self.ping is False:
                color = "red"
                color = "color:#FF0000;"
        else:
                color = "green"
                color = "color:#00FF00;"
        # return format_html("<span style=color:%s>%s</span>" % (color, self.addrip))
        return format_html("<a href=%s style=%s>%s</a>" % (url, color, self.addrip ))
        # return format_html('<span style=color:%s><a href="%s</a></span>' % (color, self.addrip, self.addrip))
                                    

    colored_addrip.allow_tags = True

# class Testlan(models.Model):
#     modalite = models.OneToOneField(Modalite, on_delete=models.CASCADE, primary_key=True,)
#     pingip = models.BooleanField(default=False)
#     pinghost = models.BooleanField(default=False)
#     pingdicom = models.BooleanField(default=False)# 

#     class Meta:
#         managed = True
#         db_table = 'Testlan'# 

#     def __str__(self):
#         return "IP de la modalité : {0}".format(self.modalite.aet)

