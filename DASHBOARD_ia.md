# Les pages et cartes du dashboard

Retrouvez sur cette page toutes les cartes du **Dashboard Arrosage**, ainsi que leurs fonctions et code.

##


### La page principale

<p align="center"><img src="Medias/arrosage_page.jpg"></p>

<details>
  <summary><code><img src="Medias/Icons/code.svg" width="16" align="absmiddle"> Voir le code de la page</code></summary>

<br>

📄 **Fichier :** `ui-lovelace/cards/navigation_card.yaml`

```yml

```
</details>

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### **- La carte navigation**

<p align="center"><img src="Medias/navigation_card.jpg"></p>

Cette carte permet de naviguer entre les différentes pages du **dashboard**

<img src="Medias/Icons/arrow-left.svg" width="20" align="absmiddle"> : Permet de revenir à la page précédemment affichée.

<img src="Medias/Icons/calendar-clock-outline.svg" width="20" align="absmiddle"> : Permet de naviguer vers la page **Programmation d'arrosage**. Elle sera <img src="Medias/Icons/calendar-clock-outline_green.svg" width="20" align="absmiddle"> si un calendrier nommé `Arrosage` existe sinon elle sera <img src="Medias/Icons/calendar-clock-outline_orange.svg" width="20" align="absmiddle">.

<img src="Medias/Icons/tune.svg" width="20" align="absmiddle"> : Permet de naviguer vers la page **Paramètres**.

<details>
  <summary><code><img src="Medias/Icons/code.svg" width="16" align="absmiddle"> Voir le code de la carte</code></summary>

<br>

📄 **Fichier :** `ui-lovelace/cards/navigation_card.yaml`

```yml
type: custom:mushroom-chips-card
chips:
  - type: back
  - type: template
    content: ARROSAGE
    uix:
      style: |
        ha-card {
          border: none;
          background: none !important;
        }
  - type: spacer
  - type: template
    icon: mdi:calendar-clock
    icon_color: >-
      {{ 'deep-orange' if is_state('calendar.arrosage', 'unknown') else
      'light-green' }}
    tap_action:
      action: navigate
      navigation_path: planning-arrosage
  - type: template
    icon: mdi:tune
    icon_color: deep-orange
    tap_action:
      action: navigate
      navigation_path: parametres-dashboard-arrosage
grid_options:
  columns: full
  rows: auto
```
</details>

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### **- La carte arrosage en cours**

<p align="center"><img src="Medias/arrosage_en_cours_card.jpg"></p>

Cette carte s'affichera quand un arrosage de zone est en cours.

<img src="Medias/Icons/stop.svg" width="20" align="absmiddle"> : Permet de couper l'arrosage de la zone avant son terme.

<details>
  <summary><code><img src="Medias/Icons/code.svg" width="16" align="absmiddle"> Voir le code de la carte</code></summary>

<br>

📄 **Fichier :** `ui-lovelace/cards/navigation_card.yaml`

```yml
type: conditional
conditions:
  - condition: state
    entity: input_boolean.misha_arrosage_cycle_zone_1
    state: "on"
card:
  type: custom:mod-card
  uix:
    style: |
      ha-card {
        background: #e8f3db;
        --grid-card-gap: 0x;
        border: 1px solid #dbdbdb;
      }
  card:
    type: grid
    square: false
    cards:
      - type: custom:mushroom-template-card
        multiline_secondary: true
        primary: ""
        secondary: >-
          L arrosage de la zone
          {{states('input_text.misha_arrosage_nom_de_zone_1')}}
          est en cours. Arrêt prévu à
          {{state_attr('input_datetime.misha_arrosage_duree_cycle_zone_1',
          'timestamp')| timestamp_custom("%Hh%M", true, now())}}
        icon: mdi:sprinkler-variant
        tap_action:
          action: none
        color: light-green
        features_position: bottom
        uix:
          style: |
            ha-card {
              border: none;
              background: none;
              margin-right: -100%;
              padding-right: 100px;
            }
      - type: custom:mushroom-chips-card
        chips:
          - type: template
            icon: mdi:stop
            tap_action:
              action: perform-action
              perform_action: script.misha_arrosage_arret
              data:
                zone_id: "1"
            uix:
              style: |
                ha-card {
                  border:none; 
                  --chip-border-radius: 12px;
                  --chip-background: rgba(var(--rgb-primary-text-color), 0.1);
                }
        alignment: end
        uix:
          style: |
            ha-card {
              background: none;
              padding-right: 8px;
              padding-top: 9px;
            }
    columns: 2
grid_options:
  columns: full
visibility:
  - condition: state
    entity: input_boolean.misha_arrosage_cycle_zone_1
    state: "on"

```
</details>

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### **- La carte zone**

<p align="center"><img src="Medias/zone_card.jpg"></p>

Carte indiquant le nom de la zone ainsi que son id. Elle permet entre autre de déclencher un arrosage de zone manuellement.

<img src="Medias/Icons/form-textbox.svg" width="13" align="absmiddle"> : Permet de modifier le nom de la zone.

<img src="Medias/Icons/numeric-5.svg" width="20" align="absmiddle">: Indique le nombre de voies liées à la zone (ici 5). Elle sera<img src="Medias/Icons/numeric-5_grey.svg" width="20" align="absmiddle">quand tout est bien configuré,<img src="Medias/Icons/numeric-5_red.svg" width="20" align="absmiddle">si aucune voie n'est liée à la zone et<img src="Medias/Icons/numeric-5_orange.svg" width="20" align="absmiddle">si vous avez des voies réelles et virtuelles liées à la zone.

<img src="Medias/Icons/check-network-outline.svg" width="14" align="absmiddle"> : Indique si les voies de la zone sont connectées. Elle sera <img src="Medias/Icons/check-network-outline_grey.svg" width="14" align="absmiddle"> en mode démo, <img src="Medias/Icons/check-network-outline_green.svg" width="14" align="absmiddle"> si toutes les voies de la zone sont connectées, <img src="Medias/Icons/check-network-outline_orange.svg" width="14" align="absmiddle"> si des voies de la zone sont déconnectées et <img src="Medias/Icons/check-network-outline_red.svg" width="14" align="absmiddle"> si toutes les voies de la zone sont déconnectées. Elle permet du coup de savoir si on est en mode démo ou production (icone grise ou colorée).

<img src="Medias/Icons/calendar-clock-outline.svg" width="20" align="absmiddle"> : Permet d'activer/désactiver la programmation. Elle passera <img src="Medias/Icons/calendar-clock-outline_green.svg" width="20" align="absmiddle"> si la programmation est activée et <img src="Medias/Icons/calendar-clock-outline_orange.svg" width="20" align="absmiddle"> si la programmation est activée mais qu'aucun évènement n'est prévu dans le calendrier dans les 30 jours à venir.

<img src="Medias/Icons/sprinkler-variant.svg" width="20" align="absmiddle"> : Permet de déclencher un arrosage de zone. Elle passera en <img src="Medias/Icons/sprinkler-variant_green.svg" width="20" align="absmiddle"> quand une zone est en cours d'arrosage.
<br><br>

Cette carte dispose également de ces propres notifications.
<p align="center"><img src="Medias/zone_card_notifs.jpg"></p>

<details>
  <summary><code><img src="Medias/Icons/code.svg" width="16" align="absmiddle"> Voir le code de la carte</code></summary>

<br>

📄 **Fichier :** `ui-lovelace/cards/navigation_card.yaml`

```yml



```
</details>

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### **- La carte voie**

<p align="center"><img src="Medias/voie_card.jpg"></p>

*<p align="center">La carte sans arrosage en cours</p>*

<p align="center"><img src="Medias/voie_card_en_cours.jpg"></p>

*<p align="center">La carte avec arrosage en cours</p>*

Carte indiquant le nom de la voie et son id ainsi que la date et l'heure du dernier arrosage. Elle permet de déclencher la voie et également de la liée à une zone.

<img src="Medias/Icons/sprinkler-variant.svg" width="20" align="absmiddle"> : Permet de déclencher/arrêter la voie. Elle passe en <img src="Medias/Icons/sprinkler-variant_cyan.svg" width="20" align="absmiddle"> lorsque un arrosage est en cours.

<img src="Medias/Icons/dots-horizontal.svg" width="12" align="absmiddle"> : Permet de lier la voie à une zone. Elle sera <img src="Medias/Icons/dots-horizontal_orange.svg" width="12" align="absmiddle"> si la voie est n'est pas liée à une zone, sinon elle sera <img src="Medias/Icons/dots-horizontal_green.svg" width="12" align="absmiddle">.

<img src="Medias/Icons/check-network-outline.svg" width="14" align="absmiddle"> : Indique si la voie est connectée. Elle sera <img src="Medias/Icons/check-network-outline_grey.svg" width="14" align="absmiddle"> en mode démo, sinon <img src="Medias/Icons/check-network-outline_green.svg" width="14" align="absmiddle"> si la voie est connectée, et <img src="Medias/Icons/check-network-outline_red.svg" width="14" align="absmiddle"> si la voie est déconnectée. Elle permet du coup de savoir si on est en mode démo ou production (icone grise ou colorée) toute comme la même icone sur la carte zone.

<img src="Medias/Icons/timer.jpg"> : Permet de régler la durée de déclenchement de la voie.

<img src="Medias/Icons/check-circle-outline.svg" width="20" align="absmiddle"> : Permet de sélectionner/déselectionner la voie pour un cycle d'arrosage de zone. Elle passe en <img src="Medias/Icons/check-circle-outline_green.svg" width="20" align="absmiddle"> lorsque la voie est sélectionnée ou <img src="Medias/Icons/close-circle-outline_grey.svg" width="20" align="absmiddle"> si cela n'est pas le cas.
<br><br>

Comme la carte zone, cette carte dispose de ces propres notifications.
<p align="center"><img src="Medias/voie_card_notifs.jpg"></p>

<details>
  <summary><code><img src="Medias/Icons/code.svg" width="16" align="absmiddle"> Voir le code de la carte</code></summary>

<br>

📄 **Fichier :** `ui-lovelace/cards/navigation_card.yaml`

```yml



```
</details>

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### **- La carte informations programmation**

<p align="center"><img src="Medias/informations_card.jpg"></p>

La première carte indiquent les arrosages à venir par zone et la seconde renvoi la page de programmation d'arrosage.

Cette carte dispose aussi de ces propres notifications.
<p align="center"><img src="Medias/informations_card_notifs.jpg"></p>

<img src="Medias/Icons/help-circle-outline.svg" width="20" align="absmiddle"> : Renvoi vers la page documentation du **dashboard arrosage**. Les autres icones renvoient vers les pages adéquates de **Home Assistant**.

<details>
  <summary><code><img src="Medias/Icons/code.svg" width="16" align="absmiddle"> Voir le code de la carte</code></summary>

<br>

📄 **Fichier :** `ui-lovelace/cards/navigation_card.yaml`

```yml



```
</details>

<p align="center"><img src="Medias/Icons/divider.png"></p>


#### **- La carte information connectivité**

<p align="center"><img src="Medias/connectivity_card.jpg"></p>

Une carte grid, regroupant les cartes de connectivité de chaque zone.

<img src="Medias/Icons/check-network-outline.svg" width="20" align="absmiddle"> : Indique si les voies de la zone sont connectées. Elle sera <img src="Medias/Icons/check-network-outline_grey.svg" width="20" align="absmiddle"> en mode démo, <img src="Medias/Icons/check-network-outline_green.svg" width="20" align="absmiddle"> si toutes les voies de la zone sont connectées, <img src="Medias/Icons/check-network-outline_orange.svg" width="20" align="absmiddle"> si des voies de la zone sont déconnectées et <img src="Medias/Icons/check-network-outline_red.svg" width="20" align="absmiddle"> si toutes les voies de la zone sont déconnectées. Elle permet du coup de savoir si on est en mode démo ou production (icone grise ou colorée).

<details>
  <summary><code><img src="Medias/Icons/code.svg" width="16" align="absmiddle"> Voir le code de la carte</code></summary>

<br>

📄 **Fichier :** `ui-lovelace/cards/navigation_card.yaml`

```yml

```
</details>

##


### La page programmation arrosage

<p align="center"><img src="Medias/programmation_page.jpg"></p>

Sur cette page vous pouvez définir la programmation de chaque zone en cliquant sur le bouton <img src="Medias/Icons/ajout_event.png" width="100" align="absmiddle">

On retrouve en haut de la page une carte de navigation comme sur la page principale. Cette carte est utile si vous souhaitez faire de cette page une `sous-vue` sur votre dashboard.

La section `informations complémentaires` comprend des informations utiles pour l'ajout d'évènements au calendrier d'arrosage.

<details>
  <summary><code><img src="Medias/Icons/code.svg" width="16" align="absmiddle"> Voir le code de la page</code></summary>

<br>

📄 **Fichier :** `ui-lovelace/cards/navigation_card.yaml`

```yml

```
</details>

##


### La page paramètres

<p align="center"><img src="Medias/parameters_page.jpg"></p>

On retrouve en haut de la page une carte de navigation comme sur la page principale. Cette carte est utile si vous souhaitez faire de cette page une `sous-vue` sur votre dashboard.

La section `Paramètres` permet de choisir où vous voulez envoyer les notifications.

La section `Mode de fonctionnement` indique si vous êtes en mode **démo** ou **production**. En mode production elle listera la correspondance entre les voies du dashboard et votre matériel.

La section `Mode de fonctionnement` Permet l'ajout ou la suppression de voies ou de zones en cliquant sur les boutons correspondants.

En cas d'ajout/suppression une carte apparaitra, indiquant qu'il est nécessaire de redémarrer le srveur pour prendre en compte les modifications.

<p align="center"><img src="Medias/restart_needed_card.jpg"></p>

En cas de suppression et après redémmarage du serveur, une carte listant les entités orphelines apparaitra, pour vous rappeler de les supprimer.

<p align="center"><img src="Medias/entites_orphelines_card.jpg"></p>

Cette carte se masquera une fois les entités orphelines supprimées.

<details>
  <summary><code><img src="Medias/Icons/code.svg" width="16" align="absmiddle"> Voir le code de la page</code></summary>

<br>

📄 **Fichier :** `ui-lovelace/cards/navigation_card.yaml`

```yml

```
</details>

<hr>
