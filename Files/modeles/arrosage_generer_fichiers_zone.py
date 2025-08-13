import os
import re
import sys

# Chemins
script_dir = os.path.dirname(os.path.abspath(__file__))
dossier_source = script_dir  # modeles
dossier_destination = os.path.dirname(script_dir)  # arrosage

# Fichier source
fichier_source_entities = os.path.join(dossier_source, "zone_x.txt")
fichier_source_automation = os.path.join(dossier_source, "automatisation_arrosage_zone_x.txt")

# --- Étape 1 : trouver le numéro suivant ---
max_num = 0
pattern = re.compile(r"zone_(\d+)\.yaml$")

for fichier in os.listdir(dossier_destination):
    match = pattern.match(fichier)
    if match:
        num = int(match.group(1))
        if num > max_num:
            max_num = num

numero = max_num + 1

# --- Étape 2 : vérifier si le fichier existe déjà ---
nom_sortie_entities = f"zone_{numero}.yaml"
fichier_destination_entities = os.path.join(dossier_destination, nom_sortie_entities)
nom_sortie_automation = f"automatisation_arrosage_zone_{numero}.yaml"
fichier_destination_automation = os.path.join(dossier_destination, nom_sortie_automation)

if os.path.exists(fichier_destination_entities):
    print(f"⚠️ Fichier {fichier_destination_entities} existe déjà.", file=sys.stderr)
    sys.exit(1)
if os.path.exists(fichier_destination_automation):
    print(f"⚠️ Fichier {fichier_destination_automation} existe déjà.", file=sys.stderr)
    sys.exit(1)

### Fichier  entrées
# --- Étape 3 : lire et modifier le modèle ---
try:
    with open(fichier_source_entities, "r", encoding="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print(f"❌ Modèle {fichier_source_entities} introuvable.", file=sys.stderr)
    sys.exit(1)

contenu_modifie_entities = contenu.replace("[X]", str(numero))

# --- Étape 4 : sauvegarder ---
os.makedirs(dossier_destination, exist_ok=True)
with open(fichier_destination_entities, "w", encoding="utf-8") as f:
    f.write(contenu_modifie_entities)
###

### Fichier  automatisation
# --- Étape 3 : lire et modifier le modèle ---
try:
    with open(fichier_source_automation, "r", encoding="utf-8") as f:
        contenu = f.read()
except FileNotFoundError:
    print(f"❌ Modèle {fichier_source_automation} introuvable.", file=sys.stderr)
    sys.exit(1)

contenu_modifie_automation = contenu.replace("[X]", str(numero))

# --- Étape 4 : sauvegarder ---
os.makedirs(dossier_destination, exist_ok=True)
with open(fichier_destination_automation, "w", encoding="utf-8") as f:
    f.write(contenu_modifie_automation)    
###

# --- Étape 5 : sortie pour Home Assistant ---
print(numero)  
#print(f"✅ Fichier créé : {nom_sortie_automation}", file=sys.stderr)
