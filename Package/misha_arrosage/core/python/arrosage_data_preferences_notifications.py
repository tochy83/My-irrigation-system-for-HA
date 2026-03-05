# Script de sauvegarde des choix d'appareils, utilisateurs pour les notifications.

import json
import sys
import os

file_path = "/config/packages/misha_arrosage/core/data/arrosage_data_preferences_notifications.json"

arg1 = sys.argv[1].strip() if len(sys.argv) > 1 else ""
arg2 = sys.argv[2].strip() if len(sys.argv) > 2 else ""

# Sauvegarde dans un JSON, si on a des données
if arg1 != "" and arg2 != "":
    payload = {"mobile_app": arg1, "telegram": arg2}
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)

# Lecture du Json (toujours nécessaire pour le retour vers HA)
if os.path.exists(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(f"{data.get('mobile_app','pas de notifications')}|{data.get('telegram','pas de notifications')}")
else:
    print("pas de notifications|pas de notifications")