from django.core.management.base import BaseCommand
import subprocess
from imagerie.models import Modalite

class Command(BaseCommand):
    args = ''
    help = "retourne le résultat d' un seul ping !"

    def handle(self, *args, **options):
        # start_response('200 OK', [('Content-Type', 'text/plain')])
        import ping3
        modalites = Modalite.objects.all().order_by('addrip')
        for modal in modalites:
            if modal.ping :
                print(modal.addrip, " déjà notée joignable ",)
            else :
                try:
                    res = ping3.ping(modal.addrip, timeout=1)
                    if res:
                        modal.ping = True
                        modal.save()
                    print(modal.addrip, "  ", modal.ping )
                except:
                    print(f"---> ping problématique sur la modalité : {modal.addrip}")
