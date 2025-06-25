from apscheduler.schedulers.background import BackgroundScheduler
from .ping_all_update import *

def start():
    intervalle = 3600           #  21600 sec = 6h
    print("===>>  On lance avec le timer la commande <ping_all_update> du lundi au vendredi, de 8 à 18 h00 toutes les 2 heures     <<=== ")
    scheduler = BackgroundScheduler()
    
    # toute les heures :
    # scheduler.add_job(pingall, 'interval', seconds=intervalle)
    
    # du lundi au vendredi, de 10 à 16 h00 toutes les 2 heures :
    scheduler.add_job(pingall, 'cron', day_of_week= 'mon-fri', hour='8,10,12,14,16,18') 
    # du lundi au vendredi, à 19h00 après tous les <pingall> précédemment lancés, on lance le nettoyage des doublons sur l' historique :
    scheduler.add_job(histo_clean_duplicate, 'cron', day_of_week= 'mon-fri', hour='19')  
    
    # du lundi au vendredi, toutes les 5 minutes [ pour test ] :
    # scheduler.add_job(pingall, 'cron', day_of_week= 'mon-fri', minute= '*/5')  
    
    scheduler.start()