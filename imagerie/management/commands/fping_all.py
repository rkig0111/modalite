from django.core.management.base import BaseCommand
from imagerie.models import Modalite
from django.utils import timezone
from pathlib import Path
from modalite.settings import BASE_DIR
from asyncio import run
import imagerie.adminextra as admx 
import time

class Command(BaseCommand):
    args = ''
    help = "Scanne les modalités pour noter celles qui répondent au ping et met à jour la BDD, version asyncio/aioping"

    def horodat(self):
        return timezone.now().strftime('%Y/%m/%d, %H:%M:%S')

    def handle(self, *args, **options):
        import ping3
        modalites = Modalite.objects.all()  # .order_by('addrip')
        listip = []
        for i in modalites:
            listip.append(i.addrip) 
        listipunique = list(set(listip))
        listoflist = []
        for x in listipunique:
            x = [x]
            listoflist.append(x)
        fic = Path(BASE_DIR / 'private/ping_all.txt')  
        listeping = []    
        with open(fic, "a") as result:
            # result.write(f"{timezone.now().strftime('%Y/%m/%d, %H:%M:%S')}")  
            listeping = run(admx.main(listoflist))    
            # print("listeping --->  ", listeping)
            count = 0
            for modal in listeping:
                ip = modal[1]      #  adresse ip
                ping = modal[0]    #  True  ou  False  
                delai = modal[2]   #  delai de réponse du ping. non utilisé actuellement        
                modalbdd = Modalite.objects.filter(addrip=ip)
                for m in  modalbdd:          
                    if (m.ping == False) and (ping == True):
                        # print(f"---> {count} la modalité {m.addrip} répond pour la première fois au ping                                    ")  
                        m.ping = True
                        m.first_ping = timezone.now()
                        result.write(f"{self.horodat()} la modalite {m.addrip} repond pour la premiere fois au ping\n")                        
                    elif (m.ping == True) and (ping == True):
                        # print(f"---> {count} la modalité {m.addrip} répond au ping et a déjà répondu au ping                                    ") 
                        m.recent_ping = timezone.now()                        
                    elif (m.ping == True) and (ping == False):
                        # print(f"---> {count} la modalité {m.addrip} a déjà répondu pas au ping mais à l' air : éteinte? réformée? en panne? ")                        
                        pass                    
                    elif (m.ping == False) and (ping == False) :
                        # print(f"---> {count} la modalité {m.addrip} n'a pour l'instant, jamais répondu au ping                              ")
                        count += 1
                        pass

                    #m.save()

            modal_ON = Modalite.objects.filter(ping=True).count()
            modal_OFF = Modalite.objects.filter(ping=False).count()   
            result.write(f"{self.horodat()} --> ON : {modal_ON}  ---  OFF : {modal_OFF} \n")
            # print(f"{self.horodat()} --> ON : {modal_ON}  ---  OFF : {modal_OFF} \n")

