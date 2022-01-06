# Projet AlgoInvest&Trade

## Description:
Vous vous apprêtez à utiliser une application permettant de sélectionner une liste d'actions uniques, les plus rentables parmis une série d'actions disponibles dans un fichier .csv et selon un budget limité.

---

## Fichiers .csv:

- Fichier brute_force.csv, qui contient 20 actions et sur lequel s'exécute nos algorithmes de force brute et recursif
    
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

- L'algorithme de force_brute qui crée toutes les combinaisons possibles, les trie et choisit celle qui nous rapporte le plus de profit sans dépasser un budget alloué. Il est gourmand en puissance de calculs, ce qui constitue sa limite d'utilisation.

- L'algorithme recursif, crée un arbre de décisions dans le même but que son concurrent force brute. Il est plus rapide à exécuter mais lui aussi limité dans son utilisation sur un dataset plus large.
    
- L'algorithme dynamique, pour qui chaque sous-solutions d'une solution optimale est optimale, parcours un champ de données fixe, ce qui lui permet de s'exécuter incroyablement plus vite.

