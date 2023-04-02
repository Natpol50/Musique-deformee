class Faudio:
    """
    Classe correspondant à un fichier audio dans le problème 4 de l'édition 2023 du TFJM²
    
    Pour créer un nouveau fichier, il faut faire comme ceci :
    
>>> fichier_original = Faudio(("saumon","orange","silence","rouge"))

    Pour afficher le fichier, il faut faire comme ceci :

>>> fichier_original.affiche_fichier()

1/4 = saumon
2/4 = orange
3/4 = silence
4/4 = rouge

    Pour afficher la résolution du fichier, il faut faire comme ceci :
    
>>> fichier_original.affiche_resolution()

4
    
    
    Pour changer de résolution, il faut utiliser changement_de_resolution, dont voici un exemple de l'utilisation en utilisant les valeurs des 3 exemples précédents :
    
>>> fichier_original.changement_de_resolution(8)

>>> fichier_original.affiche_resolution()

8

>>> fichier_original.affiche_fichier()

1/8 = saumon
2/8 = saumon
3/8 = orange
4/8 = orange
5/8 = silence
6/8 = silence
7/8 = rouge
8/8 = rouge

    """
    def __init__(self,notes):
        self.res = len(notes)   # On initialise la résolution à la longueur de la liste de notes
        self.file =  {}         # On crée un dictionnaire vide qui va contenir le fichier audio
        count = 1               # On initialise un compteur à 1
        for i in range(0, self.res):     # Pour chaque note dans la liste de notes
            self.file[f"{count}/{self.res}"] = notes[i]    # On ajoute la note au dictionnaire avec une clé sous la forme "numéro de note/résolution totale"
            count += 1      # On incrémente le compteur
    
    def affiche_fichier(self):
        for k in range(0, self.res):    # Pour chaque note dans le fichier audio
            print(f"{k+1}/{self.res} = {self.file[f'{k+1}/{self.res}']}")     # On affiche la clé et la valeur du dictionnaire
    
    def affiche_resolution(self):
        print(self.res)     # On affiche la résolution
    
    def value(self, pos, res):
        pos = 2*pos-1    # On calcule la position de la note dans le nouveau fichier audio
        res_2 = 2*res    # On calcule la nouvelle résolution
        for i in range(0, self.res):     # Pour chaque note dans le fichier audio original
            if (i+1)/self.res < pos/res_2:   # Si la note est avant la position de la nouvelle note
                True
            elif (i+1)/self.res > pos/res_2:    # Si la note est après la position de la nouvelle note
                return self.file[f"{(i+1)}/{self.res}"]     # On retourne la note correspondante dans le fichier audio original
            elif (i+1)/self.res == pos/res_2:    # Si la note est à la position de la nouvelle note
                return 'silence'    # On retourne silence
    
    def changement_de_resolution(self, m):
        self.new = {}     # On crée un nouveau dictionnaire vide
        count2 = 1        # On initialise un compteur à
