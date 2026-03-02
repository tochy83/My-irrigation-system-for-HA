# Les pages et cartes du dashboard

Retrouvez sur cette page toutes les cartes du **Dashboard Arrosage**, ainsi que leur fonctions et code.

---

### La page principale

<p align="center">
<img src="Medias/arrosage_page.jpg" width="100%">
</p>

#### **1️⃣ La carte navigation**

<p align="center">
<img src="Medias/navigation_card.jpg" width="100%">
</p>

Cette carte permet de naviguer entre les différentes pages du **dashboard**

<details>
  <summary>Le code <span><img src="Medias/Icons/code.svg" width="18"></span></summary>

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

<p align="center">
<img src="Medias/Install/verify.jpg" width="45%" alt="Vérification OK">
<img src="Medias/Install/verify_not_ok.jpg" width="45%" alt="Vérification KO">
</p>

---

#### **2️⃣ Activation des Packages**

Vérifiez si les packages sont actifs dans votre `configuration.yaml`. Ouvrez le fichier et recherchez la ligne suivante sous la clé `homeassistant:` :

```yaml
homeassistant:
  packages: !include_dir_named packages

```

*Si elle n'existe pas, ajoutez-la, vérifiez la configuration et redémarrez Home Assistant.*

> [!TIP]
> Pour en savoir plus sur l'intérêt des packages, consultez cet [article sur Domo-blog.fr](https://www.domo-blog.fr/packages-home-assistant-organiser-configuration-code-yaml-domotique/).


> [!NOTE] 
> Il est possible, si vous utilisez déjà les packages mais de manière différente et que vous ayez la ligne :
> ```
>packages: !include_dir_merge_named packages/
> ```
> Dans ce cas il y a quelques modifications à faire pour rendre l'intégration instalable.
---

#### **3️⃣ Téléchargement**

Téléchargez le fichier ZIP contenant l'intégration depuis la [page d'accueil du repository](https://github.com/tochy83/My-irrigation-system-for-HA).

<p align="center"><img src="Medias/Install/download_from_github.gif" alt="Download GitHub"></p>

---

#### **4️⃣ Transfert des fichiers**

1. À l'aide de **Studio Code Server**, créez un dossier `packages` dans `/config/`.
2. Copiez le dossier `misha_arrosage` du ZIP dans le dossier `packages` que vous venez de créer.

<p align="center">
<img src="Medias/Install/studio_code_server_add_folder.gif" width="45%">
<img src="Medias/Install/studio_code_server.gif" width="45%">
</p>

**Structure finale attendue :**

<p align="center"><img src="Medias/Install/structure_dossier_packages.jpg" alt="Structure dossiers"></p>

---

#### **5️⃣ Redémarrage du serveur**

Pour finaliser l'installation, il faut maintenant redémarrer Home Assistant. Allez dans **Paramètres > Outils de développement > YAML** et cliquez sur `Vérifier la configuration`. Si le message `La configuration n'empêchera pas Home Assistant de démarrer !` apparait, vous pouvez cliquer sur `Redémarrer` puis `Redémarrer Home Assistant`.

> [!IMPORTANT]
> Si le message `La configuration n'empêchera pas Home Assistant de démarrer !` n'apparaissait pas il est probable que vous ayez fait une erreur à l'étape 2️⃣ ou 4️⃣.
> Vérifiez donc ces 2 étapes.
---
#### **6️⃣ Mise en place du Dashboard**

1. Créez un nouveau Dashboard nommé **Arrosage** (respectez la casse, des liens internes l'utilisent).
2. Ouvrez le fichier `dashboard.yaml` (présent dans le ZIP), copiez tout son contenu et collez-le dans l'éditeur de configuration de votre nouveau dashboard.

<p align="center"><img src="Medias/Install/add_dashboard.gif" alt="Ajout Dashboard"></p>

---

#### **7️⃣ Configuration du Calendrier**

Ajoutez l'intégration **Calendrier local** (si vous ne l'utilisez pas déja) et créez un calendrier nommé exactement `Arrosage`.

<p align="center">
<img src="Medias/Install/add_local_calendar_int.gif" width="45%">
<img src="Medias/Install/add_calendar.gif" width="45%">
</p>

> [!NOTE] 
> Si vous avez déjà un calendrier nommé `Arrosage`, c'est celui-ci qui sera utilisé.
---

#### **8️⃣ Liaison avec Calendar Merge**

Configurez une entrée pour l'intégration **Calendar Merge**.
**C'est cette étape qui permet l'affichage des arrosages à venir.**

* **Nom du capteur :** `misha arrosage a venir` (Strictement !)
* **Période :** 7 jours
* **Nombre max d'événements :** Votre nombre de zone
* **Calendrier :** Arrosage
* **Option :** Désactiver "Utiliser le résumé comme nom d’entité"
* **Format de date :** Selon votre préférence

<p align="center">
<img src="Medias/Install/add_calendar_merge_int.gif" width="45%">
<img src="Medias/Install/config_calendar_merge.gif" width="45%">
</p>

---

### 🎉 C'est fini !

Il ne vous reste plus qu'à tester toutes les fonctionnalités. Pour la partie programmation, ajoutez simplement des événements au calendrier comme montré dans la vidéo ci-dessous.

> [!NOTE]
> L'intégration tourne actuellement en **mode simulation** pour vous permettre de découvrir le fonctionnement sans activer vos vannes réelles.

<div align="center">

  [![Lancer la vidéo](https://img.youtube.com/vi/Ewms74Tb5es/0.jpg)](https://www.youtube.com/watch?v=Ewms74Tb5es "Lancer la vidéo")

</div>

*<p align="center">Une vidéo complète de l'installation pas à pas en partant d'un Home Assistant vierge ou j'ai juste installé tous les modules complémentaires et intégrations nécessaires à l'installation et au fonctionnement du Dashboard. La seule différence avec les étapes décrites ci-dessus est que je passerai par l'explorateur de fichiers windows pour créer les différents dossiers nécessaires au packages et copier les fichiers car c'est plus rapide pour la vidéo.</p>*
<br><br><br><br><br>
