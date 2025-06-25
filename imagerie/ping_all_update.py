from modalite.settings import BASE_DIR, SUBJECT01, MAIL_FROM, MAIL_TO, MAIL_SRV, MAIL_SRV_PORT
from imagerie.models import Modalite
from django.utils import timezone
from django.core import management
from simple_history.management.commands import clean_duplicate_history
import smtplib
from email.message import EmailMessage
import logging
import ping3
from pathlib import Path
import time

global boucle
boucle = 0

# ping_all_update.py  permet de mettre les champs first_ping et last_ping de la BDD modalite à jour.
# besoin de la librairie 'apscheduler' (pip install ou poetry add) pour lancer ce script à intervalle régulier.

logging.basicConfig(filename='ping_all_auto.log',level=logging.INFO)
   
def send_msg(data):   
    debuglevel = 0    
    message = " résultat de la commande ping_all_auto.py. \n"

    msg = EmailMessage()
    msg.set_content(message + data)    
    
    msg['Subject'] = SUBJECT01
    msg['From'] = MAIL_FROM
    msg['To'] = MAIL_TO

    s = smtplib.SMTP(MAIL_SRV, MAIL_SRV_PORT)  # si pas d'envoi mail, demander à la DSN si autorisation accordée pour cette machine. (IP)
    s.set_debuglevel(debuglevel)
    s.send_message(msg)
    s.quit()

def horodat():
    return timezone.now().strftime('%Y/%m/%d %H:%M:%S')

def histo_clean_duplicate():    
    management.call_command('clean_duplicate_history', '--auto')
    # print(f"le nettoyage des doublons de la Base de données historique a été réalisé... ")
    return
    
def pingall():
    global boucle
    boucle += 1
    new_modal = ""
    modalites = Modalite.objects.all()               # .order_by('addrip')
    # modalites = Modalite.objects.filter(addrip__startswith='172.16.52.')  # .order_by('addrip')  [ pour test ! ]
    fic = Path(BASE_DIR / 'private/ping_all.txt')   
    count = 0     
    with open(fic, "a") as result:
        #result.write(f"{timezone.now().strftime('%Y/%m/%d, %H:%M:%S')}")      
        for modal in modalites:
            count += 1
            try:
                res = ping3.ping(modal.addrip, timeout=1)
                print(f"{count:4d} : {modal.addrip:<16}  ---->  {res} sec.                          ", flush=True, end="\r")   # "\x0d\x0a"
                if res and (modal.ping == True) :                    
                    modal.recent_ping = timezone.now()
                    # print(f"---> {count:4d} la modalité {modal.addrip:<16} répond au ping et a déjà répondu au ping                                ", end="\x0d\x0a")
                    # new_modal = new_modal + f"{horodat()}  la modalite {modal.addrip:<16} répond au ping et a déjà répondu au ping \n"
                elif res and  (modal.ping == False):
                    modal.ping = True
                    modal.first_ping = timezone.now()
                    # print(f"---> {count:4d} la modalité {modal.addrip:<16} répond pour la première fois au ping                                    ", end="\x0d\x0a")
                    result.write(f"{horodat()}  la modalite {modal.addrip:<16} répond pour la première fois au ping\n")
                    new_modal = new_modal + f"{horodat()}  la modalite {modal.addrip:<16} répond pour la première fois au ping\n"
                elif (res == None) and (modal.ping == True) :
                    # print(f"---> {count:4d} la modalité {modal.addrip:<16} a déjà répondu au ping mais à l' air : éteinte? réformée? en panne?     ", end="\x0d\x0a")
                    # new_modal = new_modal + f"{horodat()}  la modalite {modal.addrip:<16} a déjà répondu au ping mais à l' air : éteinte? réformée? en panne? \n"
                    pass
                elif (res == None)and (modal.ping == False) :
                    # print(f"---> {count:4d} la modalité {modal.addrip:<16} n'a, pour l'instant, jamais répondu au ping                              ", end="\x0d\x0a")
                    # new_modal = new_modal + f"{horodat()}  la modalite {modal.addrip:<16} n'a, pour l'instant, jamais répondu au ping  \n"
                    pass
                modal.save()
            except:
                if "0.0.0" in modal.addrip:
                    pass
                else:
                    result.write(f"{horodat()} --> problème d' accès à la modalité : {modal.addrip} \n")
                    # print(f"---> {count} la modalité {modal.addrip} a un problème d' accès !                                                ") 
        modal_ON = Modalite.objects.filter(ping=True).count()
        modal_OFF = Modalite.objects.filter(ping=False).count()   
        result.write(f"{horodat()} --> ON : {modal_ON}  ---  OFF : {modal_OFF} \n")
        data = new_modal + f"{boucle:3d} -- {horodat()}  --> ON : {modal_ON}  ---  OFF : {modal_OFF} \n"
        # print(data)
        
        if new_modal:
            send_msg(data)
      
