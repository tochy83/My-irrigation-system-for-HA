
**La page arrosage** (Sans arrosage en cours) :
<p align="center"><img src="../Medias/arrosage_page.jpg" width=75%></p>
<br><br>

**La page arrosage** (Avec arrosage en cours) :
<p align="center"><img src="../Medias/arrosage_page_arrosage_en_cours.jpg" width=75%></p>
<br><br>

**La page calendrier** :
<p align="center"><img src="../Medias/calendrier_page.jpg" width=75%></p>

<details>
  <summary>Le code de la page : (Cliquer pour afficher)</summary>

```yml
type: sections
max_columns: 2
title: Planning arrosage
path: planning-arrosage
icon: mdi:calendar
sections:
  - type: grid
    cards:
      - type: custom:mushroom-chips-card
        chips:
          - type: back
          - type: template
            content: PROGRAMMATION ARROSAGE
            double_tap_action:
              action: none
            tap_action:
              action: none
            hold_action:
              action: none
            card_mod:
              style: |
                ha-card {
                  border: none;
                  background: transparent !important;
                }
        grid_options:
          columns: full
          rows: auto
    column_span: 2
  - type: grid
    cards:
      - type: custom:mod-card
        card:
          type: custom:mushroom-title-card
          title: ""
          subtitle: Calendrier d'arrosage
        card_mod:
          style:
            mushroom-title-card$: |
              .subtitle {
                border-bottom: 1px solid var(--ha-card-border-color,var(--divider-color,#e0e0e0));
                padding-bottom: 0px;
              }
              .header {
                margin-bottom: -7px;
              }
      - type: calendar
        entities:
          - calendar.arrosage
      - type: custom:mushroom-chips-card
        chips:
          - type: template
            tap_action:
              action: navigate
              navigation_path: /calendar
            icon: mdi:plus
            icon_color: white
            content: ""
        alignment: end
        card_mod:
          style: |
            ha-card {
              --chip-background: #0CACF4;
              --chip-border-color: #0CACF4;
              --primary-text-color: white;
              padding-right: 8px;
            }
  - type: grid
    cards:
      - type: custom:mod-card
        card:
          type: custom:mushroom-title-card
          title: ""
          subtitle: Infos complémentaires
        card_mod:
          style:
            mushroom-title-card$: |
              .subtitle {
                border-bottom: 1px solid var(--ha-card-border-color,var(--divider-color,#e0e0e0));
                padding-bottom: 0px;
              }
              .header {
                margin-bottom: -7px;
              }
      - type: markdown
        content: >-
          - Pour ajouter une programmation cliquez sur l'icone <font color
          ="#0cacf4"><ha-icon icon="mdi:plus-circle"></ha-icon></font> sous le
          calendrier.<br><br>

          - Pour modifier/supprimer une programmation vous pouvez cliquez
          directement dessus dans le calendrier ci-contre/ci-dessus.<br><br>

          - **<font color =orange>Attention</font>**, tout ajout ou modification
          à un délai de 15 minutes avant d'être pris en compte.<br><br>

          - **<font color =orange>Attention</font>**, pour une prise en compte
          de la programmation, bien penser à mettre **<font color =orange>le nom
          </font>** de la zone d'arrosage concernée comme résumé du
          calendrier.<br><br>

          - Pour rappel, les noms de vos zones sont :

          {% for item in states.sensor.arrosage_noms_des_zones.attributes |
          select('match', 'zone_') -%}

          Pour la {{ item | replace('_',' ') }} : **<font color =orange>{{
          state_attr('sensor.arrosage_noms_des_zones' , item) }}</font>**

          {% endfor %}
        card_mod:
          style: |
            ha-card {
              color: var(--secondary-text-color);
              background: none;
              border: 0;
            }
              ha-markdown.no-header {
              padding-bottom: 0px !important;
            }      
cards: []
```
</details>
<br><br>
