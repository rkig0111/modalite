## projet modalite

> au préalable, une installation de python, git et de poetry est requise...

### 1. créez le dossier de projets (repos_modalite par exemple) :

```
    mkdir repos_modalite
    cd mkdir repos_modalite
```

### 2. Cloner le projet

```
    git clone https://github.com/rkig0111/modalite
```

> aller dans le répertoire "modalite" qui vient d’ être créé.
> [ BASEDIR pour Django et répertoire de travail de « vscode » ]

```
    cd modalite
```

### 3. installer l' environnement virtuel

```
    poetry install --no-root
```

> on peut passer sous VSCODE et le paramétrer avec l' environnement virtuel fraichement créé pour notre application.

### 4. install de la BDD et choix de celle-ci ( parametrage dans instance_settings.py )

#### ---> 4.1 soit on part sur une BDD vierge :

```
    DATABASES = {
    "default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": BASE_DIR / "db2.sqlite3",
    }}
```

```
    python manage.py migrate            # création des tables dans la BDD
```

#### ---> 4.2 soit on va récupérer la BDD où j’ai fait une récupération du logiciel d' imagerie ( récupération rapide sans tri :-( ):

```
    copy \\serveur_biomed\repertoire_partage\db2.sqlite3 .
```

> attention, il y a un espace entre le sqlite3 et le point !

#### ---> 4.3 soit on utilise la BDD réelle (production):

```
    DATABASES = {
    "default": {
    "ENGINE": "django.db.backends.sqlite3",
    "NAME": "//serveur_biomed/repertoire_partage/db2.sqlite3",
    }}
```

> remplacer <//serveur_biomed> et <repertoire_partage> par leur vrai valeur !!!

### 5. création du superuser :

```
    python manage.py createsuperuser
```

### 6. lancement du serveur :

> lancer le serveur et se connecter à http://127.0.0.1:8000/ (redirigé vers http://127.0.0.1:8000/admin/)
> on peut paramétrer avec < http://127.0.0.1:8000/admin/imagerie/modalite/?reforme__exact=0 >
> pour afficher directement toutes les modalités sans les réformes

```
    python manage.py runserver
```

> y’a plus qu’à… ! :-)

<br>
<br>

### pour planifier le script ping_all_update.py sur son poste et pour le développement :

décommenter dans imagerie\apps.py

```
def ready(self):
	from . import updater
	updater.start()
```

> en lancant < manage.py runserver > cela lance l' update automatiquement avec les valeurs contenues dans la ligne du fichier < imagerie/updater.py >

```
    scheduler.add_job(pingall, 'cron', day_of_week= 'mon-fri', hour='8,10,12,14,15,16')
```

>                                du lundi au vendredi, de 8 à 16 h00 toutes les 2 heures
