


### Lexique

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


### Les libellés de zone

C'est grâce au libellés (labels) que les cycles d'arrosage qu'ils soient programmés ou manuels fonctionnent. Pour cela il est important que chaque zone ait son libellé et que ce libellé soit supprimer si on supprime une zone.

Le nom des libellés a également son importance. Ils doivent être de la forme Zone 1, Zone 2 et ainsi de suite. 

Je n'ai malheureusement pas trouvé comment les créer ou les supprimer automatiquement. 

### Inclure une voie à une zone 

Pour inclure une voie à une zone d'arrosage et ainsi permettre son déclenchement lors d'un cycle d'arrosage, automatique ou manuel, il faut ajouter un libellé de zone (voir Les libellés de zone) au script (script.arrosage_declenchement_auto_voie_X) X représentant le numéro de la voie à inclure dans la zone.

Cette opération se fait par l'UI de Home Assistant.

ajouter ou supprimer une voie

vous pouvez vous servir des outils présents en bas de la page paramètres documentation de l'intégration 
les outils permettent de générer les fichiers d'entités les scripts et les automatisations nécessaires au fonctionnement des voies et des zones. 

 pour ajouter une voix
 
en se servant des outils générer les fichiers nécessaires et faites un redémarrage de votre assistant pour que les entités créaient soit pris en compte 
suite à ça vous n'avez plus qu'à ajouter une carte streamline card arrosage voie sur le dashboard 

pour supprimer une voix

on supprime la carte de la voix sur le dashboard
en se servant des outils vous pouvez supprimer les fichiers d'entités pour une voix.
l'outil supprimera automatiquement la dernière fois connue
par exemple l'intégration par défaut à 9 voies si je décide d'en supprimer une l'outil supprimera la voie numéro 9.
suite à la suppression des entités orphelines seront générés. une carte du dasboard
dans la partie outil vous indiquera lesquels. vous pouvez alors passer par paramètres appareil service entité pour les supprimer complètement de la base de données 
c'est là qu'il est pratique d'avoir défini un libellé ou une catégorie pour les entités de l'intégration à l'installation de celle-ci 

ajouter ou supprimer une zone 

par défaut l'intégration vient avec 9 zones pré configuré dont 3 sont activés 

pour ajouter une zone 

servez-vous des outils présents sur la page paramètres documentation du dashboard pour générer les fichiers nécessaires à la création des entités pour une zone. 
modifier dans le fichier zones.yaml
ajouter un libellé pour cette nouvelle zone 
faites un redémarrage de home assistant

si vous désirez avoir plus de 9 zones.

il faudra en plus des étapes précédentes modifier certaines scripts et automatisation pour les prendre en compte 
faire la liste des automatisations et script ainsi que décrire les manipulations à faire

pour supprimer une zone 

 pour supprimer une zone les étapes sont les mêmes que pour supprimer une voix. 
 il faudra en plus supprimer le libellé de la zone et modifier le fichier zones.yaml pour modifier son nom.
 vous pouvez également supprimer les cartes de notification pour la zone supprimée mais ce n'est pas obligatoire.


note sur l'outil de suppression 

l'outil de suppression ne sera en mesure d'effacer les automatisations et scripts que si ceci n'ont pas été migrés dans l'interface de mon assistant. 
dans ce cas il faudra les supprimer manuellement par l'interface utilisateur de homme assistant
