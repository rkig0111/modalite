from django.core.management.base import BaseCommand
from imagerie.models import Modalite
from django.utils import timezone
from pathlib import Path
from modalite.settings import BASE_DIR

class Command(BaseCommand):
    args = ''
    help = "Scanne les modalités pour noter celles qui répondent au ping et met à jour la BDD"

    def handle(self, *args, **options):
        # start_response('200 OK', [('Content-Type', 'text/plain')])
        import ping3
        # modalites = Modalite.objects.filter(addrip__startswith="10.208.37.15").order_by('addrip')
        modalites = Modalite.objects.all()  # .order_by('addrip')
        count = 0
        fic = Path(BASE_DIR / 'private/ping_all.txt')        
        with open(fic, "a") as result:
            result.write(f"{timezone.now().strftime('%m/%d/%Y, %H:%M:%S')}")      
            for modal in modalites:
                # count += 1
                try:
                    res = ping3.ping(modal.addrip, timeout=1)
                    # print("res = ", res, "   modal.ping = ", modal.ping)
                    if res and (modal.ping == True) :                    
                        modal.recent_ping = timezone.now()
                        # print(f"---> {count} la modalité {modal.addrip} répond au ping et a déjà répondu au ping                                ", end="\x0d")
                    elif res and  (modal.ping == False):
                        modal.ping = True
                        modal.first_ping = timezone.now()
                        # print(f"---> {count} la modalité {modal.addrip} répond pour la première fois au ping                                    ")
                        result.write(f"{timezone.now()}  la modalite {modal.addrip} repond pour la premiere fois au ping\n")
                    elif (res == None) and (modal.ping == True) :
                        # print(f"---> {count} la modalité {modal.addrip} a déjà répondu pas au ping mais à l' air : éteinte? réformée? en panne? ")
                        pass
                    elif (res == None)and (modal.ping == False) :
                        # print(f"---> {count} la modalité {modal.addrip} n'a pour l'instant, jamais répondu au ping                              ", end="\x0d")
                        pass
                    modal.save()
                except:
                    pass
                    # print(f"---> {count} la modalité {modal.addrip} a un problème d' accès !                                                ")
            # print() 

            modal_ON = Modalite.objects.filter(ping=True).count()
            modal_OFF = Modalite.objects.filter(ping=False).count()    
            result.write(f" --> ping machines : {modal_ON} et {modal_OFF} qui ne repondent pas !\n")