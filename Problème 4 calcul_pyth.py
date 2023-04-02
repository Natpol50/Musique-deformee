class Faudio:
    """
    Classe correspondant à un fichier audio dans le problème 4 de l'édition 2023 du TFJM
    
    Pour créer un nouveau fichier, il faut faire comme ceci :
    
>>> fichier_original = Faudio(("saumon","orange","silence","rouge"))

    Pour afficher le fichier, il faut faire comme ceci :

>>> f.affiche_fichier()

1/4 = saumon
2/4 = orange
3/4 = silence
4/4 = rouge

    Pour afficher la résolution du fichier, il faut faire comme ceci :
    
>>> f.affiche_resolution()

4
    
    
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

"""
    def __init__(self,notes):
        self.res = len(notes)
        self.file =  {}
        count = 1
        for i in range(0, self.res):
            self.file[f"{count}/{self.res}"] = notes[i]
            count += 1
    
    def affiche_fichier(self):
        for k in range(0, self.res):
            print(f"{k+1}/{self.res} = {self.file[f'{k+1}/{self.res}']}")
    
    def affiche_resolution(self):
        print(self.res)
    
    def value(self, pos, res):
        pos = 2*pos-1
        res_2 = 2*res
        for i in range(0, self.res):
            if (i+1)/self.res < pos/res_2:
                True
            elif (i+1)/self.res > pos/res_2:
                return self.file[f"{(i+1)}/{self.res}"]
            elif (i+1)/self.res == pos/res_2:
                return 'silence'
    
    def changement_de_resolution(self, m):
        self.new = {}
        count2 = 1
        for i in range(0, m):
            self.new[f"{count2}/{m}"] = self.value(count2, m)
            count2 += 1
        self.file = self.new
        self.res = m
