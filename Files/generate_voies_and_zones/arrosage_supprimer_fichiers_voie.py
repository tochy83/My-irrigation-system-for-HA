import os
import re
import sys

# Chemins
#script_dir = os.path.dirname(os.path.abspath(__file__))
#dossier_destination = os.path.dirname(script_dir)  # packages/arrosage
DOSSIER = "/config/packages/arrosage/voies_and_zones" # Dossier où se trouve les fichiers à supprimer

# --- Trouver le dernier numéro de voie ---
max_num = 0
pattern = re.compile(r"voie_(\d+)\.yaml$")

for fichier in os.listdir(DOSSIER):
    match = pattern.match(fichier)
    if match:
        num = int(match.group(1))
        if num > max_num:
            max_num = num

if max_num == 0:
    print("⚠️ Aucun fichier voie_X.yaml trouvé.", file=sys.stderr)
    sys.exit(1)

if max_num == 1:
    print("⚠️ Vous ne pouvez pas supprimer les fichiers de la voie 1.", file=sys.stderr)
    sys.exit(1)

# --- Liste des fichiers à supprimer ---
fichiers_a_supprimer = [
    os.path.join(DOSSIER, f"voie_{max_num}.yaml"),
    os.path.join(DOSSIER, f"script_arrosage_declenchement_auto_voie_{max_num}.yaml"),
    os.path.join(DOSSIER, f"automatisation_arrosage_voie_{max_num}.yaml"),
]

# --- Suppression ---
suppr_ok = True
for fichier in fichiers_a_supprimer:
    if os.path.exists(fichier):
        try:
            os.remove(fichier)
            print(f"🗑️ Supprimé : {os.path.basename(fichier)}", file=sys.stderr)
        except Exception as e:
            print(f"❌ Erreur suppression {os.path.basename(fichier)} : {e}", file=sys.stderr)
            suppr_ok = False
    else:
        print(f"ℹ️ Absent : {os.path.basename(fichier)}", file=sys.stderr)

# --- Sortie pour Home Assistant ---
if suppr_ok:
    print(max_num)  # stdout
else:
    sys.exit(1)
