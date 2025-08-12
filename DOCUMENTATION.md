les libellés de zone

c'est grâce au libellé que les cycles d'arrosage qu'il soit programmé ou manuel fonctionne. 
c'est pour ça qu'il est important que chaque zone ai son libellé et que se libellé se supprimer si on supprime une zone 
le nom des libellé a également son importance ils doivent être de la forme Zone 1, Zone 2 et ainsi de suite. 
je n'ai malheureusement pas trouvé comment les créer ou les supprimer automatiquement. 

inclure une voix à une zone 

pour inclure une fois à une zone d'envers il faut ajouter un libellé de zone (voir libellé de zone) au script déclenchement auto voie x x représentant le numéro de la voie

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


note sur l'outil de suppression 

l'outil de suppression ne sera en mesure d'effacer les automatisations et scripts que si ceci n'ont pas été migrés dans l'interface de mon assistant. 
dans ce cas il faudra les supprimer manuellement par l'interface utilisateur de homme assistant
