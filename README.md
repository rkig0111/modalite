projet modalite

au préalable, une installation de git est requise...

1.  créez le dossier de projets (repos_modalite par exemple) :

    mkdir repos_modalite  
    cd mkdir repos_modalite

2.  Cloner le projet

    git clone https://github.com/rkig0111/modalite

    aller dans le répertoire "modalite" qui vient d’ être créé. [ BASEDIR pour Django et répertoire de travail de « vscode » ]
    cd modalite

3.  installer l' environnement virtuel

    poetry install --no-root (tiret tiret no tiret root tout collé)

    pour vérifier que c' est fonctionne, lancer : < python manage.py check > il ne devrait pas y avoir d' erreur !

    on peut passer sous VSCODE ou tout autre outil de développement.

4.  install de la BDD et choix de celle-ci

    - soit on part sur une BDD vierge :
      [ poetry shell # pour lancer l'environnement virtuel ] devient optionnel
      python manage.py migrate # création des tables dans la BDD
      python manage.py createsuperuser # création du superuser pour accéder à l'administration de django  
       python manage.py runserver # lancer le serveur de développement et se connecter à http://127.0.0.1:8000/admin

    - soit on va récupérer la BDD où j’ai fait une récupération du logiciel d' imagerie ( récupération rapide ):  
       ( pour faire les tests, c’est mieux )

    copy \\serveur_biomed\repertoire_partage\db2.sqlite3 . # attention, il y a un espace entre le sqlite3 et le point !

    y’a plus qu’à… ! :-)

pour planifier le script ping_all_update.py sur son poste et pour le développement :

décommenter dans imagerie\apps.py
def ready(self):
from . import updater
print("modalite/imagerie/apps.py ( ImagerieConfig.ready )")
updater.start()

en lancant < manage.py runserver --noreload > il lance l' update automatiquement avec les valeur de la ligne du fichier < imagerie/updater.py >

    scheduler.add_job(pingall, 'cron', day_of_week= 'mon-fri', hour='8,10,12,14,15,16')  # du lundi au vendredi, de 8 à 16 h00 toutes les 2 heures

ne fonctionne pas, nous n' avons pas les droits adéquats !

# aller dans le planificateur de tache

# créer une tache.

# par exemple pour moi :

#

# Command : C:\Users\kligliro\AppData\Local\pypoetry\Cache\virtualenvs\repos-modalite-btVqF2Tu-py3.10\Scripts\python.exe

# Arguments : C:\Users\kligliro\repos_modalite\modalite\manage.py ping_all

# WorkingDirectory: C:\Users\kligliro\repos_modalite\modalite
