# Musique-derformee
Projet d'automatisation du calcul de nouveau fichier dans le but de résoudre le Problème 4 de l'édition 2023 du TFJM
Classe correspondant à un fichier audio dans le problème 4 de l'édition 2023 du TFJM
    
    
 ## Création de fichier    
 
    Pour créer un nouveau fichier, il faut faire comme ceci :

>>> fichier_original = Faudio(("saumon","orange","silence","rouge"))

## Affichage de fichier
    Pour afficher le fichier, il faut faire comme ceci :

>>> f.affiche_fichier()

1/4 = saumon
2/4 = orange
3/4 = silence
4/4 = rouge

## Affichage de résolution du fichier
    Pour afficher la résolution du fichier, il faut faire comme ceci :
    
>>> f.affiche_resolution()

4
    
## Changement de résolution du fichier  

    Pour changer de résolution, il faut utiliser changement_de_resolution, dont voici un exemple de l'utilisation en utilisant les valeurs des 3 exemples précédents :
    
>>> f.changement_de_resolution(8)

>>> f.affiche_resolution()

8

>>> f.affiche_fichier()

1/8 = saumon
2/8 = saumon
3/8 = orange
4/8 = orange
5/8 = silence
6/8 = silence
7/8 = rouge
8/8 = rouge


---

[CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/)

2023
