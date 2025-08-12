


#### - Lexique

Parce que chaque culture/plantation a son propre besoin en eau, il faut bien comprendre le rôle du calendrier,  des voies d'arrosage, des zones d'arrosage et des cycles d'arrosage pour appéhender le fonctionnement de l'ensemble.
- Calendrier : Le calendrier contient les jours et heures de départ d'arrosage ainsi que le nom de la zone concernée (les événements). C'est lui qui définit **la fréquence d'arrosage** d'une zone.

- Voie d'arrosage : Une voie d'arrosage correspond à un ensemble électrovanne (ou autre système de commande) + tuyau + goutteurs (asperseurs, buses...) permettant l'arrosage d'une culture/plantation.
C'est sur la voie d'arrosage qu'on définit **la durée** d'ouverture de l'électrovanne et par conséquence **la quantité d'eau délivrée à chaque culture/plantation** présente sur cette voie.

- Zone d'arrosage : Une zone d'arrosage correspond à un groupe d'une ou plusieurs voies d'arrosage. Chaque voie d'arrosage incluse dans une même zone aura donc la même fréquence d'arrosage.

- Cycle d'arrosage de zone : Un cycle d'arrosage de zone pilote le déclenchement successif de chaque voie comprise dans la zone.

Pour résumé :
- On définit dans le calendrier les jours et heures de départ d'arrosage ainsi que le nom de la zone concernée (les événements).
- Lorsque la date présente correspond à un événement du calendrier, un ordre est envoyé pour declencher un arrosage de la zone renseignée dans l'événement du calendrier.
- Cet ordre déclenchera un cycle d'arrosage de la zone concernée.
- Le déclenchement du cycle ouvrira chaque éléctrovanne correspondante aux voies incluses dans la zone concernée, pour la durée définie pour chaque voie.
- L'ouverture de chaque éléctrovanne se fait en cascade, d'abord la première pour la durée que l'on aura choisi avant de passer à la seconde et ce jusqu'à la dernière incluse dans la zone.

On garde bien sûr la possibilité de déclencher un cycle ou une voie de façon manuelle.
<br><br>


#### - Les libellés de zone

C'est grâce au libellés (labels) que les cycles d'arrosage qu'ils soient programmés ou manuels fonctionnent. Pour cela il est important que chaque zone ait son libellé et que ce libellé soit supprimer si on supprime une zone.

Le nom des libellés a également son importance. Ils doivent être de la forme Zone 1, Zone 2 et ainsi de suite. 

Je n'ai malheureusement pas trouvé comment les créer ou les supprimer automatiquement. 
<br><br>


#### - Inclure une voie à une zone d'arrosage

Pour inclure une voie à une zone d'arrosage et ainsi permettre son déclenchement lors d'un cycle d'arrosage, automatique ou manuel, il faut ajouter un libellé de zone (voir Les libellés de zone) au script (script.arrosage_declenchement_auto_voie_X) X représentant le numéro de la voie à inclure dans la zone.

Cette opération se fait par l'UI de Home Assistant.
<br><br>


#### - Ajouter une nouvelle voie d'arrosage

Pour ajouter une voie d'arrosage un outil est présent dans la page paramètres de "l'intégration". Il permet de générer les fichiers d'entités, les automatisations et les scripts nécessaires au fonctionnement d'une voie d'arrosage. 

Une fois les fichiers générés, il faudra redémarrer Home Assistant pour que la nouvelle voie puisse être utilisée. Vous pouvez ajouter plusieurs voies avant le redémarrage de Home assistant.

Suite à ça vous n'avez plus qu'à ajouter une carte 'custom:streamline-card avec le template arrosage_voie' pour cette nouvelle voie sur le dashboard.
<br><br>


#### - Supprimer une voie d'arrosage

Pour supprimer une voie d'arrosage un bouton est présent dans la page paramètres de "l'intégration". Il permet de supprimer les fichiers d'entités, les automatisations et les scripts nécessaires au fonctionnement d'une voie d'arrosage.

Après suppression des fichiers, il faudra redémarrer Home Assistant. On supprime ensuite la carte de la voix sur le dashboard.
<br><br>


#### - Ajouter une zone d'arrosage

Par défaut l'intégration vient 3 zones actives et 6 autres zones qui n'attendent que leurs entités.

Pour ajouter une zone d'arrosage un outil est présent dans la page paramètres de "l'intégration". Il permet de générer les fichiers d'entités et les automatisations nécessaires au fonctionnement d'une zone d'arrosage.

Une fois les fichiers générés, il faudra activer la ou les nouvelles zones (Voir Activer/Désactiver une zone d'arrosage) et comme vu précédemment ajouter un libellé pour les nouvelles zones (Voir Les libellés de zone) avant d'enfin redémarrer Home Assistant pour leur prise en compte.

Suite à ça vous n'avez plus qu'à ajouter une carte 'custom:streamline-card avec le template arrosage_zone' pour cette nouvelle zone sur le dashboard.
<br><br>


#### - Si vous avez besoin de plus de 9 zones.

Il faudra en plus des étapes précédentes modifier certains scripts et automatisations pour en tenir compte.

Le script à modifier est :
- script.arrosage_arret

Les automatisations à modifier sont :
- automation.arrosage_zone_x (x représentant le numéro de la nouvelle zone)
- automation.arrosage_calendrier
- automation.arrosage_nombre_electrovannes_incluses_par_zone
- automation.arrosage_affichage_notifications_temporaires
- automation.arrosage_alerte

Les modifications à effectuées sont dans le descriptif du script et des automatisations.

Il faudra également ajouter au dashboard les cartes notifications correspondantes à ces nouvelles zones en dupliquant celles existantes et en modifiant le numéro de zone à l'intérieure de celles-ci.
<br><br>


#### - Pour supprimer une zone 

 Pour supprimer une zone les étapes sont les mêmes que pour supprimer une voie.
 
 Il faudra en plus supprimer le libellé de la zone (Voir Les libellés de zone) et désactiver cette zone.
 
 Vous pouvez également supprimer les cartes de notification pour la zone supprimée (mais ce n'est pas obligatoire).
<br><br>

#### - Note sur les outils de suppression de voie et de zone.

L'outil de suppression de voie ou de zone, permet de supprimmer les fichiers d'entités, les automatisations et les scripts nécessaires au fonctionnement d'une voie ou d'une zone d'arrosage.

Il supprime les fichiers de la dernière voie ou zone existante. Ex. Si j'ai 9 voies d'arrosage il supprimera les fichiers de la voie 9.

L'outil de suppression ne sera en mesure d'effacer les automatisations et scripts, que si ceci n'ont pas été migrés dans l'UI de Home Assistant. Dans ce cas, il faudra les supprimer manuellement par l'interface utilisateur de Home Assistant.

Suite à la suppression des fichiers par l'outil, des entités orphelines peuvent apparaitre.

Une carte du dasboard, sur la page paramètres donne une liste de celles-ci le cas échéant. Cette carte n'est pas visible s'il n'y à pas d'entités orphelines liées à "l'intégration". Vous pouvez alors passer par Paramètres/Appareils et services/Entités pour les supprimer complètement de Home Assistant.

C'est là qu'il est pratique d'avoir défini un libellé ou une catégorie pour toutes les entités de l'intégration à l'installation de celle-ci, pour les retrouver plus rapidement.
<br><br>


#### - Activer/Désactiver une zone







