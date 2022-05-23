# Notre projet:
Créer une figure artistique grâce au jeu de la vie.
## __Participants__ 
Samuel Nonon, Yohann Pouillieute

## __Informations sur le jeu de la vie:__
![exemple jeu de la vie](http://www.makery.info/wp-content/uploads/2015/08/ao%C3%BBt-01-2015-2330.gif)

Le jeu de la vie est un automate cellulaire dont les règles ont été définies par J. Conway en 1970. L'état de l'automate à l'étape n est uniquement fonction de son état à l'étape n − 1. L'évolution de l'état d'une cellule dépend de l'état de ses 8 plus proches voisins. Dans l'automate de Conway, les règles sont les suivantes : 
* Une cellule vide à l'étape n − 1 et ayant exactement 3 voisins sera occupée à l'étape suivante. (naissance liée à un environnement optimal) 
* Une cellule occupée à l'étape n − 1 et ayant 2 ou 3 voisins sera maintenue à l'étape n sinon elle est vidée. (destruction par désertification ou surpopulation) 

C'est l'analogie entre ces règles et certains critères d'évolution de populations de bactéries qui a conduit à donner à cet automate le nom de jeu de la vie.   

*Pour plus d'informations sur le jeu de la vie voici quelques liens:*
* [wikipedia du jeu de la vie](https://fr.wikipedia.org/wiki/Jeu_de_la_vie)
* [lien d'un site pour jouer](https://playgameoflife.com)


## __Modules utilisés:__
             
* PyQt5
* time
* threading
* os
* sys
* json
* random

## __Fichiers nécessaires:__
Pour faire fonctionner notre projet, il faut récupérer tout le contenu en faisant un zip:
* cliquer sur l'onglet vert 'code' puis appuyer sur 'download ZIP'



## __Affichage et création des figures:__ 
Pour poser des points nous avons rentrer:
* d'abord à la main toutes les coordonées des points pour faire apparaitre des mots:
```
cases [i + 68] [j + 11] ['s'] = life_status
        cases [i + 68] [j + 11] ['c'] = color
        cases [i + 68] [j + 12] ['s'] = life_status
        cases [i + 68] [j + 12] ['c'] = color

```
* puis à l'aide d'une fonction:
```
for i in range (17, 42, 24) :
            for j in range (29, 54) :
                cases [i + 10] [j] ['s'] = life_status
                cases [i + 10] [j] ['c'] = color
```
*Les différents bug possible*
* faire apparaitre une fenetre trop grande(taille changeable dans data), on vous conseille pour notre projet la taille préexistante
* 





