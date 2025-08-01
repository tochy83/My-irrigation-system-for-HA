# Installation

Vous trouverez sur cette page toutes les explications nécessaires à la mise en place du Dashboard arrosage ainsi que de toutes les automatisations, scripts, entrées utiles à son bon fonctionnement.
<br><br>

#### Les modules complémentaires nécessaires pour installer le dashboard :
* 'File Editor' ou 'Studio Code Server'
* Si vous avez en plus 'Samba share' c'est un plus pour la copie des fichiers (C'est bien plus rapide qu'avec File Editor)
<br><br>

#### Integrations nécessaires au fonctionnment du dashboard arrosage :

* Calendrier local disponible dans les intégrations de base de HA
* Les [mushrooms card](https://github.com/piitaya/lovelace-mushroom?tab=readme-ov-file#-mushroom) disponibles sur HACS
* [Card mod 3](https://github.com/thomasloven/lovelace-card-mod?tab=readme-ov-file#card-mod-3) disponible sur HACS
* [Vertical stack in card](https://github.com/ofekashery/vertical-stack-in-card?tab=readme-ov-file#vertical-stack-in-card) disponible sur HACS
* [Timer bar card](https://github.com/rianadon/timer-bar-card?tab=readme-ov-file#timer-bar-card) disponible sur HACS
* [Calendar merge](https://github.com/kgn3400/calendar_merge?tab=readme-ov-file#calendar-merge-helper) disponible sur HACS
* Et bien sur HACS pour pouvoir installer tout ce que je viens de lister ci-dessus
<br><br>

**Pour bénéficier de la réception des notifications** envoyées par "l'intégration", il faut avoir installé également **l'application sur son smartphone ou une tablette**.
Ce n'est pas une obligation mais dans ce cas là vous n'aurez simplement pas de notifications. De toute façon, par défaut elles sont désactivées.
<br>

Je précise également que le script des notifications a été ecrit pour des appareils tournant sous ANDROID. Je ne sais pas quelle sera sont comportement sous IOS puisque les 2 plateformes ne supportent pas les mêmes fonctionnalités pour les notifications (tout du moins dans leur syntaxe). Je suppose que si vous utilisez déjà cette fonctionnalité sur votre appareil IOS, vous saurez adapter le script à celui-ci.
<br>

Il est, à mon avis, facilement adaptable pour télégram également.
<br><br>


**Pour coller au plus grand nombre, toutes les étapes de l'installation que je vais décrire seront réalisées avec File Editor.**
<br><br>

### Les différentes étapes de l'installation :

#### - ***Etape 1*** :
Vérifier que tous les modules complémentaires et les intégrations nécessaires (voir le listing ci-dessus) sont installés sur votre instance de Home Assitant.
<br>
Je ne rentrerai pas ici dans les détails de comment installer tout ça. Je pars du principe que si vous en êtes à faire des "dashboards avancés", c'est que vous maitrisez cette partie. Si ce n'est pas le cas dans les liens que j'ai mis il y'a en général toutes les explications nécessaires et dans tous les cas ces sujets ont été abordés à maintes reprises sur le [forum HACF](https://forum.hacf.fr/).
<br><br>

S'assurer que vous n'avez pas d'entités sur votre instance Home Assistant ayant les même 'entity_id' que ceux que l'on s'apprête à installer.
<br>

Pour ça, on se rend dans Outils de développement/Modèle et on copie dans l'éditeur de modèle tous le bloc de code ci-dessous :
```yml
Entités en commun avec Arrosage :
{%- set boolean = (states['input_boolean'] | selectattr('entity_id','match','input_boolean.arrosage_') |map(attribute='entity_id') | list ) %}
{%- set text = (states['input_text'] | selectattr('entity_id','match','input_text.arrosage_') |map(attribute='entity_id') | list ) %}
{%- set number = (states['input_number'] | selectattr('entity_id','match','input_number.arrosage_') |map(attribute='entity_id') | list ) %}
{%- set datetime = (states['input_datetime'] | selectattr('entity_id','match','input_datetime.arrosage_') |map(attribute='entity_id') | list ) %}
{%- set sensor = (states['sensor'] | selectattr('entity_id','match','sensor.arrosage_') |map(attribute='entity_id') | list ) %}
{%- set binary_sensor = (states['binary_sensor'] | selectattr('entity_id','match','binary_sensor.arrosage_') |map(attribute='entity_id') | list ) %}
{%- set timer = (states['timer'] | selectattr('entity_id','match','timer.arrosage_') |map(attribute='entity_id') | list ) %}
{%- set switch = (states['switch'] | selectattr('entity_id','match','switch.arrosage_') |map(attribute='entity_id') | list ) %}
{%- set automation = (states['automation'] | selectattr('entity_id','match','automation.arrosage_') |map(attribute='entity_id') | list ) %}
{%- set script = (states['script'] | selectattr('entity_id','match','script.arrosage_') |map(attribute='entity_id') | list ) %}
{%- set helpers = boolean|count + text|count + number|count + datetime|count + sensor|count + binary_sensor|count + timer|count + switch|count %}
Entrées : {{ helpers }}
Automatisations : {{ automation | count }}
Scripts : {{ script | count }}
{% if (helpers + automation|count + script|count) == 0 %}
Pas de soucis pour procéder à l'installation
{% else %}
Installation déconseillée en l'état. Vous avez ces entités en commun avec l'intégration :
- input_boolean : {{ iif (boolean|count > 0, boolean|join(', '), boolean|count)}}
- input_text : {{ iif (text|count > 0, text|join(', '), text|count)}}
- input_number : {{ iif (number|count > 0, number|join(', '), number|count)}}
- input_datetime : {{ iif (datetime|count > 0, datetime|join(', '), datetime|count)}}
- sensor : {{ iif (sensor|count > 0, sensor|join(', '), sensor|count)}}
- binary_sensor : {{ iif (binary_sensor|count > 0, binary_sensor|join(', '), boolean|count)}}
- timer : {{ iif (timer|count > 0, timer|join(', '), binary_sensor|count)}}
- switch : {{ iif (switch|count > 0, switch|join(', '), boolean|count)}}
- automation : {{ iif (automation|count > 0, automation|join(', '), boolean|count)}}
- script : {{ iif (script|count > 0, script|join(', '), boolean|count)}}
{% endif %}
```
<br>

Si c'est tout bon, vous devriez voir un message comme celui-ci :
<p align="center"><img src="Medias/Install/verify.jpg"></p>

Sinon le résultat ressemblera plus à ça, avec une liste de toutes les entités ayant un 'entity_id' en commun avec "l'intégration" :
<p align="center"><img src="Medias/Install/verify_pas_ok.jpg"></p>
<br>


#### - ***Etape 2*** :
Vérifier dans le fichier 'configuration.yaml' si les packages sont actifs. Si vous ne voyez pas de quoi je parle c'est que probablement vous ne les avez jamais utlisé et que du coup ils ne sont pas actifs.
A l'aide de File Editor, ouvrer le fichier 'configuration.yaml' et rechercher si il contient la ligne suivante :
```yml
  packages: !include_dir_named packages
```
Si oui c'est tout bon et vous pouvez passer directement à l'étape 3, sinon il va falloir la rajouter sous la "clé" 'homeassistant:' pour au final avoir un résultat qui ressemble à ça :
```yml
homeassistant:
  packages: !include_dir_named packages
```
Si il y a déjà d'autres lignes sous la "clé" 'homeassistant:' on les laisse bien sur et on rajoute simplement :
```yml
  packages: !include_dir_named packages
```
Une fois l'ajout effectué, on va dans Outils de développement, on vérifie la configuration pour être sur qu'il n'ya pas d'erreurs et on redémarre Home Assistant.
<br>

Pour en savoir plus sur les packages et découvrir leur intérêt, vous pouvez lire cet [article](https://www.domo-blog.fr/packages-home-assistant-organiser-configuration-code-yaml-domotique/) sur Domo-blog.fr
<br><br>

#### - ***Etape 3*** :
Depuis [la page d'accueil de ce 'repository'](https://github.com/tochy83/My-irrigation-system-for-HA) télécharger le fichier zip contenant toutes les fichiers de "l'intégration".
<p align="center"><img src="Medias/Install/download_from_github.gif"></p>

Une fois téléchargé, on les extrait dans le dossier de son choix.
<br><br>


#### - ***Etape 4*** :
A l'aide de File Editor, créer dans le dossier 'config' de Home Assistant, un dossier nommé 'packages'. Pour rappel le dossier 'config' se nomme pour File Editor 'homeassistant' et c'est le dossier où l'on se trouve par défaut quand on ouvre File Editor.
<br>

Dans ce dossier 'packages' créer un dossier 'arrosage'.
<p align="center"><img src="Medias/Install/add_folder.gif"></p>
<br>


#### - ***Etape 5*** :
A l'aide de File Editor, copier tous les fichier '.yaml' qui se trouvent dans le dossier 'Files' du zip décompressé précedemment, dans le dossier 'arrosage' que l'on vient de créer.
<p align="center"><img src="Medias/Install/add_files.gif"></p>

Sur l'animation je montre comment faire pour 2 fichiers, mais il faut bien répéter la manipulation pour tous '.yaml' présent dans le dossier. C'est à cette étape qu'avoir le module complémentaire Samba share rend bien service.
<br>

Une fois ceci fait on va dans Outils de développement, on vérifie la configuration pour être sur qu'il n'ya pas d'erreurs et on redémarre Home Assistant.
<br>

Après redemmarage on doit retrouver 15 nouvelles automatisations, 11 nouveaux scripts et les 72 entrées nécessaires à "l'intégration".
<br>

Je vous conseille d'ajouter un libellé 'Arrosage' ainsi qu'une catégorie à tout ce petit monde, cela sera plus simple pour les retrouver par la suite au milieu de toutes les entités Home Assistant.
<p align="center"><img src="Medias/Install/add_categorie.gif"></p>
<br>


#### - ***Etape 6*** :
Si il n'est pas déja actif, activer le 'sensor.home_assistant_operating_system_version'. C'est le sensor qui me sert à simuler la connectivité des électrovannes pour le mode simulation de "l'intégration".

<br>


#### - ***Etape 7*** :
Pour pouvoir recevoir les notifications, même en mode simulation, il est nécessaire de modifier le fichier '/packages/arrosage/scripts.yaml' afin d'y mettre l'id de votre téléphone ou tablette où est installée l'application mobile de Home Assistant.
<br>

Si vous ne souhaitez pas tester les notifications passer directement à l'étape 8.
<br>

A l'aide de File Editor, ouvrir le fichier '/packages/arrosage/scripts.yaml'. Aller à la ligne 533
```yml
        action: notify.mobile_app_pixel
```
Remplacer 'notify.mobile_app_pixel' par l'id de votre téléphone ou tablette.
<br>

Pour retrouver l'id de votre appareil aller à Outils de développement/Actions et chercher dans les actions 'notify.mobile', vous devriez voir la liste de tous vos appareils sur lesquels l'application mobile est installée. Dans mon cas :
<p align="center"><img src="Medias/Install/notify.jpg"></p>
Si je voulais recevoir les notifications sur ma tablette plutôt que sur mon téléphone il faudrait que je remplace 'notify.mobile_app_pixel' par :

```yml
        action: notify.mobile_app_mipad_5
```
<br>

Une fois la modification effectuée, on va dans Outils de développement, on vérifie la configuration pour être sur qu'il n'ya pas d'erreurs et on redémarre Home Assistant.
<br><br>


#### - ***Etape 8*** :
Il faut maintenant attribuer des libellés aux différents scripts 'script.arrosage_declenchement_auto_voie_[x]' pour indiquer à "l'intégration" quelle électrovannes se trouve dans quel zone.
<br>

Par defaut, puisque c'est comme ça que le Dashboard se présente il faut attribuer aux scripts :
* Pour les 'script.arrosage_declenchement_auto_voie_[x] 1,2,3,4 et 8 le libellé 'Zone 1'
* Pour les 'script.arrosage_declenchement_auto_voie_[x] 7 et 9 le libellé 'Zone 2'
* Pour les 'script.arrosage_declenchement_auto_voie_[x] 5 et 6 le libellé 'Zone 3'
<p align="center"><img src="Medias/Install/add_labels.gif"></p>
<br>

**Attention à bien respecter le noms des libellés** que j'ai donné. Autant les libellés à l'étape 5 étaient purement dans un but d'organisation, ici au contraire ils sont obligatoires au bon fonctionnement de "l'intégration".
<br><br>


#### - ***Etape 9*** :
Vient enfin la mise en place du Dashboard en lui même.
<br>

Pour ne pas risquer de casser votre Dashboard principal de Home Assistant, on va en créer un nouveau dans un premier temps. Si par la suite tout se passe bien et que l'intégration vous convient vous pourrez simplement copier ses 2 pages dans votre Dashboard principal.
<br>

A l'aide d'un éditeur de texte, ouvrir le fichier 'dashboard.yaml' situé dans le dossier 'Dashboard' du zip décompressé à l'étape 3, sélectionner tout son contenu et le copier.
<br>

Ajouter un nouveau Dashboard nommé 'Arrosage' à Home Assistant. **Ici aussi respecter le nom du calendrier** car des liens dans le Dashboard l'utilise.
<br>

Modifier ce nouveau Dashboard pour y coller le contenu du fichier 'dashboard.yaml'.
<p align="center"><img src="Medias/Install/add_dashboard.gif"></p>

Maintenant "l'intégration" est opérationnelle, il ne reste plus qu'à configurer le calendrier pour pouvoir activer la programmation.
<br><br>


#### - ***Etape 10*** :
Ajouter l'intégration 'Calendrier local si elle n'est pas déjà présente sur votre instance de Home Assistant.
<p align="center"><img src="Medias/Install/add_local_calendar_int.gif"></p>

Ajouter un calendrier nommé 'Arrosage', à l'intégration 'Calendrier local'. **Ici aussi le nom du calendrier** à son importance pour un fonctionnement "Out of the box" de "l'intégration".
<p align="center"><img src="Medias/Install/add_calendar.gif"></p>
<br>


#### - ***Etape 11*** :
Si ce n'est pas dejà fait, ajouter l'intégration 'Calendar merge'. Normalement vous auriez du le faire à l'étape 1.
<p align="center"><img src="Medias/Install/add_calendar_merge_int.gif"></p>
<br>

Configurer une entrée pour l'intégration 'Calendar merge'.
<p align="center"><img src="Medias/Install/config_calendar_merge.gif"></p>

Le fait de configurer cette intégration, va créer 5 entrées supplémentaires. Ce sont ces entrées qui permettent d'afficher les arrosages à venir du calendrier.
<br>

Dans la configuration nommer le capteur 'Arrosage a venir', il est **important de le respecter**. mettre 7 jours pour avoir les événements à venir sur une semaine, 3 en nombre maximum d'événements parce que par défaut il y'a 3 zones d'arrosage, activer 'Supprimer les événements récurrents du calendrier', choisir le calendrier 'Arrosage' et sur la seconde page, activer 'Afficher l'événement du calendrier comme heure de' et laisser le reste par défaut.
<br><br>


#### - ***Etape 12*** :
**[Voilà c'est fini](https://www.youtube.com/watch?v=EVDlleOUQXY)**
<br>

Il n'y a plus rien à faire si ce n'est de pouvoir enfin **tester toutes les fonctionnalités** de "l'intégration" 'My-irrigation-sytem-for-HA'.
<br>

Je rappelle qu'a ce stade "l'intégration" tourne en mode simulation afin que vous puissiez vous faire une idée de son fonctionnement ou de voir comment elle est construite en examinant les différents fichiers et cartes de celle-ci.
<br><br><br>



