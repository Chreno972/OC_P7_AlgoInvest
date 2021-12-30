# Projet AlgoInvest&Trade

## Description:
Vous vous apprêtez à utiliser une application permettant de sélectionner une liste d'actions uniques, les plus rentables parmis une série d'actions disponibles dans un fichier .csv et selon un budget limité.

---

## Fichiers .csv:

- Fichier brute_force.csv, qui contient 20 actions et sur lequel s'exécute nos algorithmes de force brute et de force brute recursif
    
- Deux autres fichiers , qui contiennent 1000 actions chacun et sur lesquels vont s'exécuter notre algorithme optimisé. 

---

## Installation

- Télécharger le dossier sur github, le dezziper, et les copier dans un dossier vide.
Ouvrez le avec votre éditeur de code.

**OU**

- positionnez vous dans un dossier vide et faites un git clone du projet 

**Installez un environnement virtuel et lancez le**

`python3 -m venv env` pour l'installer
`env\Scripts\activate` pour l'activer sur Windows
`source env/bin/activate` pour l'activer sur Mac

**Installer les dépendance du fichier requirements.txt**

`pip install -r requirements.txt` 

---

## Utilisation

Pour lancer un des trois algorithmes, tapez dans la console 'py nom_fichier'. Par exemple:

```shell
py brute_force.py ou py optimized_dataset1.py ou optimized_dataset2.py
```

J'ai crée deux fichiers distincts par algorithme optimisé, pour vous éviter de devoir
changer de dataset plusieurs avant de lancer le programme, car j'utilise le fichier csv
plusieurs fois dans le code.


## Les algorithmes

J'ai mis au point 3 algorithmes :

- L'algorithme de force_brute qui crée toutes les combinaisons possibles, les compare et choisit celle qui nous rapporte le plus de profit et dont la somme des prix est <= au budget alloué.
Cet algorithme est cependant très gourmand, sa complexité dans le temps est exponentielle. cest l'algorithme le plus gourmand en puissance de calculs, ce qui constitue sa limite d'utilisation.

- L'algorithme de force brute recursif, une fonction qui crée un arbre de décisions en mettant à jour la valeur de ses arguments en s'appelant à l'intérieur d'elle même. Cela permet de comparer les actions
2 par 2
Sa complexité est linéaire, ce qui le rend plus rapide à exécuter, mais aussi limité dans son utilisation sur un dataset plus large, car à mesure que la quantité d'actions à comparer augmente, le temps de complétion augmente de manière proportionnelle plusieurs occurences du même type de calcul.
    
- Le concept de cet algorithme dynamique et optimisé, nous dit que chaque sous-solutions d'une solution optimale est optimale, c’est-à-dire que le choix d'une sous-solution dans le cadre de la construction d'une solution est exhaustif.Il consiste ici à parcourir les cellules d'un tableau à deux dimensions une à une, afin d'éviter de parcourir plusieurs fois le même ensemble de données encore et encore, comme le feraient un algorithme naïf et un algorithme de force brute. Son exploitation permet de déterminer la meilleure liste d'action à acheter.
Sa complexité dans le temps est constante car elle ne dépend pas de la puissance de la machine et que nos opérations se passent uniquement à l'intérieur d'un tableau. Le gros désavantage de cet algorithme est que l'on ne peut pas avoir un profit mieux calculé car les boucles range() ne permettent pas de faire des opérations sur des floats().

