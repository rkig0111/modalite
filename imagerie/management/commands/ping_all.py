from django.core.management.base import BaseCommand
from imagerie.models import Modalite
from django.utils import timezone

class Command(BaseCommand):
    args = ''
    help = "retourne le résultat d' un seul ping !"

    def handle(self, *args, **options):
        # start_response('200 OK', [('Content-Type', 'text/plain')])
        import ping3
        # modalites = Modalite.objects.filter(addrip__startswith="10.208.37.15").order_by('addrip')
        modalites = Modalite.objects.all()  # .order_by('addrip')
        count = 0
        for modal in modalites:
            count += 1
            try:
                res = ping3.ping(modal.addrip, timeout=1)
                # print("res = ", res, "   modal.ping = ", modal.ping)
                if res and (modal.ping == True) :                    
                    modal.recent_ping = timezone.now()
                    print(f"---> {count} la modalité {modal.addrip} répond au ping et a déjà répondu au ping                                ", end="\x0d")
                elif res and  (modal.ping == False):
                    modal.ping = True
                    modal.first_ping = timezone.now()
                    print(f"---> {count} la modalité {modal.addrip} répond pour la première fois au ping                                    ")
                elif (res == None) and (modal.ping == True) :
                    print(f"---> {count} la modalité {modal.addrip} a déjà répondu pas au ping mais à l' air : éteinte? réformée? en panne? ")
                    pass
                elif (res == None)and (modal.ping == False) :
                    print(f"---> {count} la modalité {modal.addrip} n'a pour l'instant, jamais répondu au ping                              ", end="\x0d")
                    pass
                modal.save()
            except:
                print(f"---> {count} la modalité {modal.addrip} a un problème d' accès !                                                ")
        print()        
            
  