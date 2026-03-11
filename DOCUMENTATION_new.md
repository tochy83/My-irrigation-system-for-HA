# Documentation

Retrouvez sur cette page toutes les cartes du **Dashboard Arrosage**, ainsi que leurs fonctions et code.

> [!NOTE]
> Certains screenshots ou vidéos peuvent présenter de légères différences suite aux mises à jour de l'intégration. Dans ce cas une note est ajoutée à la partie concernée.

<br>

##


#### Lexique

Parce que chaque culture/plantation a son propre besoin en eau, il faut bien comprendre le rôle du calendrier,  des voies d'arrosage, des zones d'arrosage et des cycles d'arrosage pour appréhender le fonctionnement de l'ensemble.
- Calendrier : Le calendrier contient les jours et heures de départ d'arrosage ainsi que le nom de la zone concernée (les événements). C'est lui qui définit **`la fréquence d'arrosage`** d'une zone.

- Voie d'arrosage : Une voie d'arrosage correspond à un ensemble électrovanne (ou autre système de commande) + tuyau + goutteurs (asperseurs, buses...) permettant l'arrosage d'une culture/plantation.
C'est sur la voie d'arrosage qu'on définit **`la durée`** d'ouverture de l'électrovanne et par conséquence **`la quantité d'eau délivrée à chaque culture/plantation`** présente sur cette voie.

- Zone d'arrosage : Une zone d'arrosage correspond à un groupe d'une ou plusieurs voies d'arrosage. Chaque voie d'arrosage incluse dans une même zone aura donc la même fréquence d'arrosage.

- Cycle d'arrosage de zone : Un cycle d'arrosage de zone pilote le déclenchement successif de chaque voie comprise dans la zone.

Pour résumé :
- On définit dans le calendrier les jours et heures de départ d'arrosage ainsi que le nom de la zone concernée (les événements).
- Lorsque la date présente correspond à un événement du calendrier, un ordre est envoyé pour déclencher un arrosage de la zone renseignée dans l'événement du calendrier.
- Cet ordre déclenchera un cycle d'arrosage de la zone concernée.
- Le déclenchement du cycle ouvrira chaque électrovanne correspondante aux voies incluses dans la zone concernée, pour la durée définie pour chaque voie.
- L'ouverture de chaque électrovanne se fait en cascade, d'abord la première pour la durée que l'on aura choisi avant de passer à la seconde et ce jusqu'à la dernière incluse dans la zone.

On garde bien sûr la possibilité de déclencher un cycle ou une voie de façon manuelle.

<br>

##

#### - Les labels (étiquettes) de zone

C'est grâce au labels que les cycles d'arrosage  de zone, qu'ils soient programmés ou manuels fonctionnent. Pour cela, il faut lier chaque voie de la zone avec le label de celle-ci.

Les labels de zone sont créés/supprimés automatiquement à chaque ajout/suppression d'une zone et ils sont nommés **`Misha Zone x`**, x représentant le numéro de la zone.

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### - Les labels (étiquettes) de voie

C'est par les labels de voie que la liaison est faite entre voies virtuelles (mode démo) et un appareil pilotant votre arrosage.

Comme pour les labels de zone, ils sont créés/supprimés automatiquement à chaque ajout/suppression d'une voie et ils sont nommés **`Misha Voie x`**, x représentant le numéro de la voie.

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### - Lier/Enlever une voie à une zone

C'est par cette action que l'on renseigne les voies faisant partie d'une zone.

Un **`double-clic`** ou un **`appui long`** sur la partie blanche de la carte permet d'ajouter un **`label`**. Il faut ensuite effectuer un **`simple-clic`** pour mettre à jour les infos de la voie. Vous pouvez alternativement faire un **`simple-clic`** sur <img src="Medias/Icons/dots-horizontal_orange.svg" width="12" align="absmiddle"> pour ajouter le **`label`**.

Une fois liée à une zone, l’icône <img src="Medias/Icons/dots-horizontal_orange.svg" width="12" align="absmiddle"> deviendra <img src="Medias/Icons/dots-horizontal_green.svg" width="12" align="absmiddle"> avec le numéro de la zone juste à coté.

<p align="center"><img src="Medias/Personnalisation/link_voies.gif" width="75%"></p>

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### - Lier/Enlever un appareil à une voie

C'est par cette action que l'on indique au **`Dashboard arrosage`** quels appareils il doit piloter.

Une foie un appareil lié à une voie, l’icône <img src="Medias/Icons/check-network-outline_grey.svg" width="14" align="absmiddle"> deviendra <img src="Medias/Icons/check-network-outline_green.svg" width="14" align="absmiddle">ou <img src="Medias/Icons/check-network-outline_red.svg" width="14" align="absmiddle"> suivant la connectivité de l'appareil. Le changement de couleur  de l’icône permet de savoir si on est en mode démo ou production (icone grise ou colorée).


#### - Ajouter/Supprimer une voie/zone

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### - Ajouter une carte voie voie

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### - Ajouter une carte zone et les cartes liées

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### - Redémarrage du serveur

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### - Les entités orphelines

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### - Supprimer les entités orphelines

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### - Ajouter son compteur d'eau

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### - Le calcul du coefficient météo

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### - La structure des dossiers/fichiers du dashboard

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### - Passer en mode production

<p align="center"><img src="Medias/Icons/divider.png"></p>

<br><br><br><br><br>
