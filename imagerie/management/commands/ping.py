from django.core.management.base import BaseCommand
import subprocess

class Command(BaseCommand):
    args = '<team_id>'
    help = 'Affiche la liste des backlogs'

    def handle(self, *args, **options):
        # start_response('200 OK', [('Content-Type', 'text/plain')])
        proc = subprocess.Popen("./imagerie/management/commands/myscript.sh", shell=True, stdout=subprocess.PIPE)
        line = proc.stdout.readlines()
        print(line)
        self.stdout.write("coucou")
        # while line:
        #     yield line
        # line = proc.stdout.readline()
        # self.stdout.write('Coucou !')
