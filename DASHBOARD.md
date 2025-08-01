# Le dashboard arrosage

#### Integrations nécessaires à la mise du dashboard arrosage :

* Calendrier local disponible dans les intégrations de base de HA
* Les [mushrooms card](https://github.com/piitaya/lovelace-mushroom?tab=readme-ov-file#-mushroom) disponibles sur HACS
* [Card mod 3](https://github.com/thomasloven/lovelace-card-mod?tab=readme-ov-file#card-mod-3) disponible sur HACS
* [Vertical stack in card](https://github.com/ofekashery/vertical-stack-in-card?tab=readme-ov-file#vertical-stack-in-card) disponible sur HACS
* [Timer bar card](https://github.com/rianadon/timer-bar-card?tab=readme-ov-file#timer-bar-card) disponible sur HACS
* [Calendar merge](https://github.com/kgn3400/calendar_merge?tab=readme-ov-file#calendar-merge-helper) disponible sur HACS

<br><br>
*Comment installer ce dashboard sur Home assistant : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Medias/Install/add_dashboard.gif)*
<br>
*Le code du dashboard complet : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/dashboard.yaml)*
<br><br>

### La page arrosage<br><br>
<p align="center"><img src="Medias/arrosage_page.jpg" width=75%></p>
<p align="center">Une vue d'ensemble de la page arrosage.</p>
<br>


<p align="center"><img src="Medias/arrosage_page_arrosage_en_cours.jpg" width=75%></p>
<p align="center">Une vue d'ensemble de la page arrosage lorsqu'un arrosage de zone est en cours.</p>
<br>

*Le code de la page arrosage : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/arrosage_page.yaml)*
<br><br>


#### Les cartes qui la composent :


#### - ***La carte navigation*** :
<p align="center"><img src="Medias/navigation_card.jpg"></p>
Une carte qui affiche simplement le nom de la page en affichée ainsi qu'un bouton pour retourner à la page précédente.<br>
Cette carte n'est pas nécessaire au dashboard arrosage en lui même.
<br><br>

*Le code de la carte : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/navigation_card.yaml)*
<br><br>

#### - ***La carte notification*** :
<p align="center"><img src="Medias/notification_card.jpg"></p>
Cette carte affiche si un arrosage de zone est en cours. On retrouve l'heure de fin du cycle prévue ainsi qu'un bouton permettant d'arrêter l'arrosage de zone en cours.
<br><br>
L'ensemble des cartes notifications
<p align="center"><img src="Medias/notifications_card.jpg"></p>
Certaines cartes disposent de boutons qui renvoi soit vers des pages de Home Assistant soit vers des pages de ce repository.
<br><br>

*Le code de la section notifications contenant toutes les cartes : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/notification_card.yaml)*
<br><br>

#### - ***La carte zone*** :
<p align="center"><img src="Medias/zone_card.jpg"></p>
Cette carte affiche le nom de la zone d'arrosage. Elle permet de choisir si la planification doit être activée pour cette zone d'arrosage avec le bouton calendrier et également de déclencher un arrosage manuel de la zone avec le bouton "sprinkler".
<br><br>

*Le code de la carte : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/zone_card.yaml)*
<br><br>

#### - ***La carte électrovanne*** :
<p align="center"><img src="Medias/electrovanne_card.jpg"></p>
Cette carte permet de déclencher/arrêter une électrovanne manuellement avec le bouton "sprinkler".<br>
Elle permet aussi de régler la durée du cycle d'arrosage de cette électrovanne et d'inclure ou non cette électrovanne au cycle d'arrosage de la zone dans laquelle elle se trouve.<br>
Elle affiche également la date et l'heure du dernier cycle de fonctionnement l'électrovanne et volume d'arrosage du dernier cycle de fonctionnement si un dispositif de comptage d'eau est rattaché à "l'intégration".
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
<br><br>

#### - ***La carte autorisation d'envoi de notifications vers l'app mobile*** :
<p align="center"><img src="Medias/compteur_card.jpg"></p>
Cette carte à pour but d'autoriser ou non l'envoie des notifications vers l'application mobile de Home Assistant. Elle n'a pas grand intérêt en soit sur le dashboard arrosage mais lors de mes tests, avant de mettre à disposition "l'intégration," je me suis aperçu que si on ne disposait pas de l'application mobile l'envoi des notifications vers celle-ci faisait planter les automatisations (Ce qui est logique, puisque l'action notify.mobile_app n'exsiste pas dans ce cas).<br>
J'avais donc le choix soit de désactiver l'envoi de notifications dans les automatisations et scripts et libre à vous de les remettre manuellement dans chaque automatisations et scripts, soit de faire en sorte qu'elles soient activées/désactivées simplement en un clic.<br>
Voilà donc la raison d'exister de cette carte que j'ai rajouté en dernière minute.
<br><br>

*Le code de la carte : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/enable_notification_card.yaml)*
<br><br>



### La page calendrier d'arrosage<br><br>
<p align="center"><img src="Medias/calendar_page.jpg" width=75%></p>
<p align="center">Une vue d'ensemble de la page arrosage.</p>
<br>

Le code de la page calendrier : [Voir](https://github.com/tochy83/My-irrigation-system-for-HA/blob/main/Dashboard/calendar_page.yaml)
<br><br>

#### Les cartes qui la composent :


<br><br>
