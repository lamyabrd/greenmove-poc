import csv
import json

SEUIL = -2.5
evenements = []

with open("data/accelerometer_data.csv") as fichier:
    lecteur = csv.DictReader(fichier)
    for ligne in lecteur:
        acc_y = float(ligne["acc_y"])
        if acc_y < SEUIL:
            print("[FREINAGE VIOLENT]", ligne["timestamp"], acc_y)
            evenements.append({"timestamp": ligne["timestamp"], "acc_y": acc_y}) 

 
score = 100 - 10 * len(evenements)

resultat = {
    "nb_freinages_violents": len(evenements),
    "evenements": evenements,
    "score": score
}

with open("daily_score.json", "w") as fichier:
    json.dump(resultat, fichier, indent=2)

print("Score du jour :", score)