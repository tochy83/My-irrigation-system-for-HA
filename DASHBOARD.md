# Le dashboard arrosage

#### Integrations nécessaires à la mise en place du dashboard arrosage :

* Calendrier local disponible dans les intégrations de base de HA
* Les [mushrooms card](https://github.com/piitaya/lovelace-mushroom?tab=readme-ov-file#-mushroom) disponibles sur HACS
* [Card mod 3](https://github.com/thomasloven/lovelace-card-mod?tab=readme-ov-file#card-mod-3) disponible sur HACS
* [Vertical stack in card](https://github.com/ofekashery/vertical-stack-in-card?tab=readme-ov-file#vertical-stack-in-card) disponible sur HACS
* [Timer bar card](https://github.com/rianadon/timer-bar-card?tab=readme-ov-file#timer-bar-card) disponible sur HACS
* [Calendar merge](https://github.com/kgn3400/calendar_merge?tab=readme-ov-file#calendar-merge-helper) disponible sur HACS
* [Streamline card](https://github.com/brunosabot/streamline-card) disponible sur HACS


<br><br>
*Comment installer ce dashboard sur Home assistant : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Medias/Install/add_dashboard.gif)*
<br>
*Le code du dashboard complet : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/dashboard.yaml)*
<br><br>

> Certains screenshots présents ci-dessous peuvent ne pas être à jour car j'ai ajouté de nouvelles fonctionnalités depuis que j'ai rédigé cette page.
<br>

### La page arrosage<br><br>
<p align="center"><img src="Medias/arrosage_page.jpg" width=75%></p>
<p align="center">Une vue d'ensemble de la page arrosage.</p>
<br>


<p align="center"><img src="Medias/arrosage_page_arrosage_en_cours.jpg" width=75%></p>
<p align="center">Une vue d'ensemble de la page arrosage lorsqu'un arrosage de zone est en cours.</p>
<br>

*Le code de la page : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/arrosage_page.yaml)*
<br><br>


#### Les cartes qui la composent :


#### - ***La carte navigation*** :
<p align="center"><img src="Medias/navigation_card.jpg"></p>
Une carte qui affiche simplement le nom de la page en affichée et 2 boutons de navigation.<br>
<br>
<span><img src="Medias/Icons/arrow-left.svg" width="18"></span> Permet de revenir à la page précedente.
<br>
<span><img src="Medias/Icons/tune.svg" width="18"></span> Permet d'accéder à la page Paramètres/Documentation de "l'intégration".
<br><br>

*Le code de la carte : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/navigation_card.yaml)*
<br><br>

#### - ***La carte notification*** :
<p align="center"><img src="Medias/notification_card.jpg"></p>
Cette carte affiche si un arrosage de zone est en cours. On retrouve l'heure de fin du cycle prévue ainsi qu'un bouton permettant d'arrêter l'arrosage de zone en cours.
<br><br>
L'ensemble des cartes notifications
<p align="center"><img src="Medias/notifications_card.jpg"></p>
Les boutons situés sur la droite des cartes permettent certaines actions :
<br><br>
<span><img src="Medias/Icons/stop.svg" width="18"></span> Permet de couper le cycle d'arrosage de la zone en cours.
<br>
<span><img src="Medias/Icons/calendar-edit-outline.svg" width="18"></span> Renvoit sur la page calendrier de Home Asistant.
<br>
<span><img src="Medias/Icons/information.svg" width="18"></span> Renvoit vers des pages de ce repository.
<br><br>

*Le code de la section notifications contenant toutes les cartes : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/notifications_cards_section.yaml)*
<br><br>

#### - ***La carte zone*** :
<p align="center"><img src="Medias/zone_card.jpg"></p>
Cette carte affiche le nom de la zone d'arrosage. Elle permet de choisir si la planification doit être activée pour cette zone d'arrosage également de déclencher un arrosage manuel de la zone.
<br><br>
<span><img src="Medias/Icons/calendar-clock-outline.svg" width="18"></span> Permet de choisir si la planification doit être activée pour cette zone d'arrosage. Il est en vert lorsque la planification est active, en noir lorsqu'elle est inactive.
<br>
<span><img src="Medias/Icons/sprinkler-variant.svg" width="18"></span> En cliquant dessus on lance un cycle d'arrosage de la zone. Il passe alors en vert jusqu'a la fin du cycle pour indiquer qu'un cycle d'arrosage est en cours. Il ne permet pas d'arrêter le cycle d'arrosage en cours, pour cela il faut cliquer sur le bouton <span><img src="Medias/Icons/stop.svg" width="18"></span> dans la zone de notifications ou sur le bouton <span><img src="Medias/Icons/sprinkler-variant.svg" width="18"></span> de chaque carte électrovanne de la zone.
<br><br>

*Le code de la carte : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/zone_card.yaml)*
<br><br>

#### - ***La carte électrovanne*** :
<p align="center"><img src="Medias/electrovanne_card.jpg"></p>
Cette carte permet de Déclencher/Arrêter une électrovanne manuellement.<br>
Elle permet aussi de régler la durée du cycle d'arrosage de cette électrovanne et d'inclure ou non cette électrovanne au cycle d'arrosage de la zone dans laquelle elle se trouve.<br>
Elle affiche également la date et l'heure du dernier cycle de fonctionnement l'électrovanne et volume d'arrosage du dernier cycle de fonctionnement si un dispositif de comptage d'eau est rattaché à "l'intégration".
<br><br>
<span><img src="Medias/Icons/sprinkler-variant.svg" width="18"></span> Permet de Déclencher/Arrêter l'arrosage de la voie.
<br>
<span><img src="Medias/Icons/timer.jpg"></span> Permet de régler la durée de déclenchement de l'électrovanne.
<br>
<span><img src="Medias/Icons/close-circle-outline.svg" width="18"></span> / <span><img src="Medias/Icons/check-circle.svg" width="18"></span> Permettent d'inclure ou d'exclure l'électrovanne au cycle d'arrosage de sa zone. Lorsque le bouton <span><img src="Medias/Icons/close-circle-outline.svg" width="18"></span> est affiché en gris, l'électrovanne n'est pas incluse dans le cycle d'arrosage de sa zone. Quand le bouton <span><img src="Medias/Icons/check-circle.svg" width="18"></span> est affiché en vert, l'électrovanne est incluse dans le cycle d'arrosage de sa zone. Cliquer dessus bascule d'un état à l'autre.
<br><br>

*Le code de la carte : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/electrovanne_card.yaml)*
<br><br>

#### - ***La carte électrovanne*** (Avec arrosage en cours) :
<p align="center"><img src="Medias/electrovanne_card_arrosage_en_cours.jpg"></p>
Quand une électrovanne est en fonctionnement l'affichage de la carte change pour afficher le temps restant.
<br><br><br>

#### - ***La carte électrovanne*** (Avec compteur d'eau) :
<p align="center"><img src="Medias/electrovanne_card_avec_volume.jpg"></p>
Si vouz avez un sensor qui comptabilise votre consommation d'eau, la consommation du dernier cycle de l'électrovanne peut être affiché.
<br><br><br>

#### - ***La carte titre*** :
<p align="center"><img src="Medias/titre_card.jpg"></p>
Une carte qui affiche simplement un titre stylisé.
<br><br>

*Le code de la carte : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/titre_card.yaml)*
<br><br>

#### - ***La carte prochains arrosages*** :
<p align="center"><img src="Medias/prochains_arrosages_card_2.jpg" witdh="492"></p>

Cette carte récupère automatiquement les infos du calendrier d'arrosage pour les afficher. Par contre il est impératif pour qu'elle affiche quelque chose, d'avoir au préalable installer et configurer le helper [Calendar merge](https://github.com/kgn3400/calendar_merge) disponible sur HACS.
<br><br>
L'ensemble des cartes prochains arrosages
<p align="center"><img src="Medias/prochains_arrosages_cards.jpg"></p>
<br><br>

*Le code de la carte : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/prochains_arrosages_card.yaml)*
<br><br>

#### - ***La carte programmation d'arrosage*** :
<p align="center"><img src="Medias/programmation_card.jpg"></p>
Carte qui permet d'afficher la page calendrier d'arrosage.
<br><br>

*Le code de la carte : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/programmation_card.yaml)*
<br><br>

#### - ***La carte connectivité*** :
<p align="center"><img src="Medias/connectivity_card.jpg"></p>
Si vous avez un sensor qui permet de savoir si vos électrovannes sont connectées à votre serveur Home Assistant, cette carte affiche l'état de la connectivité.
<br><br>

*Le code de la carte : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/connectivity_card)*
<br><br>

#### - ***La carte compteur d'eau*** :
<p align="center"><img src="Medias/compteur_card.jpg"></p>
Si vous avez un sensor qui comptabilise votre consommation d'eau, cette carte affiche celle ci.
<br><br>

*Le code de la carte : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/compteur_card.yaml)*
<br><br><br>



### La page calendrier d'arrosage<br><br>
<p align="center"><img src="Medias/calendar_page.jpg" width=75%></p>
<p align="center">Une vue d'ensemble de la page arrosage.</p>
<br>

Le code de la page : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/parameters_page.yaml)
<br><br>
Il n'y a pas grand chose à ajouter sur cette page, elle se contente d'afficher les infos du calendrier d'arrosage ainsi que comment ajouter une programmation de zone dans le calendrier.
<br><br><br>



### La page paramètres/documentation<br><br>
<p align="center"><img src="Medias/parameters_page.jpg" width=75%></p>
<p align="center">Une vue d'ensemble de la page arrosage.</p>
<br>

Le code de la page : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/parameters_page.yaml)
<br><br>
Une page en 2 parties. Une première partie avec des paramètres à ajuster pour "l'intégration" et une seconde avec une documentation simplifiée.

#### - ***Les cartes autorisation d'envoi de notifications*** :
<p align="center"><img src="Medias/enable_mobile_notifications.jpg"></p>
Ces cartes ont pour but d'autoriser ou non l'envoie des notifications vers l'application mobile de Home Assistant ou vers Télégram.<br>
Avant d'autoriser l'envoi de notifications, assurez vous d'avoir l'application mobile d'installée et/ou l'intégration Télégram.
<br><br>
<span><img src="Medias/Icons/close-circle-outline.svg" width="18"></span> / <span><img src="Medias/Icons/check-circle-outline.svg" width="18"></span> Permettent d'autoriser ou non l'envoie des notifications vers l'application mobile de Home Assistant. Lorsque le bouton <span><img src="Medias/Icons/close-circle-outline.svg" width="18"></span> est affiché en gris, les notifications ne seront pas envoyées vers l'application mobile/Télégram. Quand le bouton <span><img src="Medias/Icons/check-circle-outline.svg" width="18"></span> est affiché en vert, les notifications seront envoyées vers l'application mobile/Télégram. Cliquer dessus bascule d'un état à l'autre.
<br><br>

*Le code de la section notifications : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/enable_notifications_cards_section.yaml)*


<br><br>
