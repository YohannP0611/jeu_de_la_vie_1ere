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


## __Interface graphique:__ (louis, yohann)


* Création d'une fenêtre avec un titre un bouton "commencer l'aventure" qui lance la fonction CreateNewWindow

![bouton commencer l'aventure](https://user-images.githubusercontent.com/91455596/154450920-27c0b2ac-292f-404f-bb2d-578d523042ad.PNG)
 
* un background avec des animations,puis un onglet déroulant offrant 2 possibilités:"nouvelle stat" et "quitter"

* quand "nouvelle stat" est choisie la fenêtre affiche des choix sur les informations contenues dans le graphique grâce à des boutons.
```
#caractéristiques des options du theme 4
case_theme4_option1 = Radiobutton(window,text ='Oui',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=1)
case_theme4_option2 = Radiobutton(window,text ='Non',bg='#FADF8F',fg='black',\
                        font=("Roman",15),activeforeground='white',
                        activebackground='#048B9A',variable=état,value=2)

    
 ```

## __Affichage et création des graphique:__ (maxence,amir)
         
* utilisation de pandas pour lire le fichier excel et pour faire un tri dans les données qui nous intéressent
* utilisation de camembert:
```
def afficher_graphique():
    x = filtres()
    plt.pie(x, labels = ['Population visée', 'Reste population'],
    colors = ['red', '#40E0D0'],
    explode = [0.3, 0],
    autopct = lambda x: str(round(x, 2)) + '%',
    pctdistance = 0.7, labeldistance = 1.4,
    shadow = True)
    plt.show()

```
*Les différents bug possible*
* animation des bulles peut faire crash la window(il suffit de relancer le programme en général ca marche, sinon raccourcir la boucle d'apparition des bulles)
* boutons mettent du temps a s'afficher (attendre l'apparition ne pas spam-click)





