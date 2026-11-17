# POC du moteur embarqué

Ce projet est une preuve de concept pour la tablette installée dans les camions. 
Il contient deux modules qui tournent en local, sans connexion internet :
- le module ZFE détecte si le camion entre dans la zone à faibles émissions de Lyon
- le module Safety repère les freinages violents à partir des données de l'accéléromètre et calcule un score de conduite.

Pour le lancer, Python suffit : je n'ai utilisé que des outils déjà inclus.

Le dossier est composé de :
- "data/lyon_polygon.json" : les coins de la zone ZFE
- "data/truck_gps.json" : les positions GPS du camion
- "data/accelerometer_data.csv" : les mesures de l'accéléromètre
- "data/accelerometer_erreurs.csv" : des mesures volontairement abîmées pour tester les erreurs
- "zfe.py" : le module 1
- "safety.py" : le module 2
- "daily_score.json" : le fichier créé par le module 2

Afin de tester le module ZFE, il faut ouvrir un terminal et entrer : python3 zfe.py

Voici le résultat obtenu :
Point 1 : OUT
Point 2 : OUT
Point 3 : OUT
[ALERT ZFE] Point 4 : IN
[ALERT ZFE] Point 5 : IN

Afin de tester le module Safety, il faut ouvrir un terminal et entrer : python3 safety.py

Voici les résultats obtenus :
[FREINAGE VIOLENT] 1678880005 -3.45
Score du jour : 90

Le programme crée également le fichier "daily_score.json" qui contient le nombre de freinages violents, les détails ainsi que le score de la journée.
Le seuil utilisé est de -2,5. 
Le score part de 100 et perd 10 points par freinage violent.

Afin de tester la gestion des erreurs, il faut entrer : python3 safety.py data/accelerometer_erreurs.csv
Ce fichier contient des lignes volontairement abîmées. Le programme les signale avec [ATTENTION] et continue sans planter. Le freinage violent est quand même détecté.
