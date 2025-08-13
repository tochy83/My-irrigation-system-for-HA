import os
import re
import json

DOSSIER = "/config/packages/arrosage/voies_and_zones" # Dossier contenat les fichiers voie_x.yaml
FICHIER_JSON = "/config/packages/arrosage/generate_voies_and_zones/arrosage_correspondance_materiel.json" # Dossier et nom du fichier json créé

pattern_fichier = re.compile(r"voie_(\d+)\.yaml$")
resultats = []

for fichier in os.listdir(DOSSIER):
    match = pattern_fichier.match(fichier)
    if match:
        numero_voie = int(match.group(1))
        chemin = os.path.join(DOSSIER, fichier)
        try:
            with open(chemin, "r", encoding="utf-8") as f:
                for ligne in f:
                    if "entity_id:" in ligne:
                        valeur = ligne.strip().replace("entity_id:", "").strip()
                        if "switch.arrosage_electrovanne_" not in valeur:
                            resultats.append({"voie": numero_voie, "entity_id": valeur})
                        break
        except FileNotFoundError:
            pass

# Tri par numéro de voie
resultats.sort(key=lambda x: x["voie"])

# Écriture au format { "json_data": [...] }
with open(FICHIER_JSON, "w", encoding="utf-8") as f:
    json.dump({"json_data": resultats}, f, ensure_ascii=False, indent=2)

print(f"Fichier JSON généré : {FICHIER_JSON}")

