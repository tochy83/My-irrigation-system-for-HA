# My-irrigation-system-for-HA
Dashboard, automations and scripts of my irrigation system for Home Assistant.

***<p align="center">Still a work in progress... it's not completely ready.</p>***

 <br><br>
Un dashboard pour Home Assistant, conçu pour 9 électrovannes réparties sur 3 zones d'arrosage. On peut bien sur ajouter ou enlever des d'électrovannes ou des zones.

<br><br>
**L'objectif de départ :**

Répliquer le fonctionnement du programmateur d'arrosage de la marque Hunter (ceux d'autres marques fonctionnant à peu de choses près de la même façon) que j'avais pour l'arrosage de mon jardin. Rendre le tout plus ergonomique et profiter des avantages de Home Assistant.

- Pouvoir déclencher l'arrosage d'une voie.
- Pouvoir régler le temps d'arrosage d'une voie.
- Pouvoir déclencher manuellement l'arrosage d'une zone (plusieurs voies).
- Faire en sorte que lors d'un arrosage de zone, chaque voie attente la fin du cycle de la précédente avant de se déclencher.
- Pouvoir établir/supprimer un planning d'arrosage de zone.
- Pouvoir inclure/exclure une voie d'un planning d'arrosage de zone.

Pour résumé, les fonctions de base de tout programmateur d'arrosage, auquel j'ai ajouté :

- Un dashboard pour piloter tout ça de manière simple et intuitive.
- L'envoi de notifications vers l'application mobile (désactivables) et/ou Télégram pour avoir un retour sur l'état du système.
> Je n'ai pas ajouté de prise en compte de capteur de pluie ou d'humidité du sol car je n'en dispose pas mais il est possible d'en tenir compte. J'aborde ce sujet ce point dans la documentation.

<br><br>
**L'objectif que je me suis fixé :**

- Laisser la possibilité à tout le monde de tester le dashboard avec un mode simulation.
- Avoir la possibilité d'interagir avec tout matériel susceptible de piloter un arrosage depuis home assistant.
- Avoir une façon relativement simple de passer du mode simulation au mode production.
- Essayer de nouvelles choses que je ne connaissais pas ou maitrisais pas sur Home Assistant.

<br><br>
**Installation :**

C'est par là que ça se passe avec les explications détaillées, étape par étape. *[Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/INSTALLATION.md)*

<br><br>
**Documentation :**

Une vue d'ensemble du Dashboard arrosage avec le code de chaque carte le composant et une description de toutes les interactions possibles avec celui-ci. *[Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/DASHBOARD.md)*

<br><br>
**Passage en production :**

Adopter le Dashboard arrosage à son sytème d'arrosage. Laisser vous guider pas à pas. *[Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/PRODUCTION.md)*

<br><br>
**Comment le supprimer :**

Vous vouliez juste tester, faire le curieux et souhaitez maintenant supprimer le Dashboard arrosage, c'est par là que cela se passe : *[Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/SUPPRESSION.md)*
