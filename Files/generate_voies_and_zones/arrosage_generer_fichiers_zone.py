import os
import re
import sys

# Chemins
#script_dir = os.path.dirname(os.path.abspath(__file__))
#dossier_source = script_dir  # modeles
#dossier_destination = os.path.dirname(script_dir)  # arrosage
DOSSIER_SOURCE = "/config/packages/arrosage/generate_voies_and_zones/modeles" # Dossier contenant les fichiers de modeles
DOSSIER_DESTINATION = "/config/packages/arrosage/voies_and_zones" # Dossier ou sont les fichiers générés depuis les modèles

# Fichier source
FICHIER_SOURCE_ENTITIES = os.path.join(DOSSIER_SOURCE, "zone_x.txt")
FICHIER_SOURCE_AUTOMATION = os.path.join(DOSSIER_SOURCE, "automatisation_arrosage_zone_x.txt")

# --- Étape 1 : trouver le numéro suivant ---
max_num = 0
pattern = re.compile(r"zone_(\d+)\.yaml$")

for fichier in os.listdir(DOSSIER_DESTINATION):
    match = pattern.match(fichier)
    if match:
        num = int(match.group(1))
        if num > max_num:
            max_num = num

NUMERO = max_num + 1

# --- Étape 2 : vérifier si le fichier existe déjà ---
NOM_SORTIE_ENTITIES = f"zone_{NUMERO}.yaml"
FICHIER_DESTINATION_ENTITIES = os.path.join(DOSSIER_DESTINATION, NOM_SORTIE_ENTITIES)
NOM_SORTIE_AUTOMATION = f"automatisation_arrosage_zone_{NUMERO}.yaml"
FICHIER_DESTINATION_AUTOMATION = os.path.join(DOSSIER_DESTINATION, NOM_SORTIE_AUTOMATION)

if os.path.exists(FICHIER_DESTINATION_ENTITIES):
    print(f"⚠️ Fichier {FICHIER_DESTINATION_ENTITIES} existe déjà.", file=sys.stderr)
    sys.exit(1)
if os.path.exists(FICHIER_DESTINATION_AUTOMATION):
    print(f"⚠️ Fichier {FICHIER_DESTINATION_AUTOMATION} existe déjà.", file=sys.stderr)
    sys.exit(1)

### Fichier  entrées
# --- Étape 3 : lire et modifier le modèle ---
try:
    with open(FICHIER_SOURCE_ENTITIES, "r", encoding="utf-8") as f:
        CONTENU = f.read()
except FileNotFoundError:
    print(f"❌ Modèle {FICHIER_SOURCE_ENTITIES} introuvable.", file=sys.stderr)
    sys.exit(1)

CONTENU_MODIFIE_ENTITIES = CONTENU.replace("[X]", str(NUMERO))

# --- Étape 4 : sauvegarder ---
os.makedirs(DOSSIER_DESTINATION, exist_ok=True)
with open(FICHIER_DESTINATION_ENTITIES, "w", encoding="utf-8") as f:
    f.write(CONTENU_MODIFIE_ENTITIES)
###

### Fichier  automatisation
# --- Étape 3 : lire et modifier le modèle ---
try:
    with open(FICHIER_SOURCE_AUTOMATION, "r", encoding="utf-8") as f:
        CONTENU = f.read()
except FileNotFoundError:
    print(f"❌ Modèle {FICHIER_SOURCE_AUTOMATION} introuvable.", file=sys.stderr)
    sys.exit(1)

CONTENU_MODIFIE_AUTOMATION = CONTENU.replace("[X]", str(NUMERO))

# --- Étape 4 : sauvegarder ---
os.makedirs(DOSSIER_DESTINATION, exist_ok=True)
with open(FICHIER_DESTINATION_AUTOMATION, "w", encoding="utf-8") as f:
    f.write(CONTENU_MODIFIE_AUTOMATION)    
###

# --- Étape 5 : sortie pour Home Assistant ---
print(NUMERO)  
#print(f"✅ Fichier créé : {NOM_SORTIE_AUTOMATION}", file=sys.stderr)
