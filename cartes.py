class Carte:
    def __init__(self, couleur, symbole):
        self.couleur = couleur
        self.symbole = symbole  
    
    def montrer(self):
        transformation = {"bleu" : "\033[94m", "rouge" : "\033[91m", "jaune" : "\033[93m", "vert" :"\033[92m" } 
        c = str(transformation.get(str(self.couleur))) + str(self.couleur)
        print(c, self.symbole)
    # ! cette fonction ne retourne rien, si utliser avec print, valeur affichée = None
    
    def peut_poser(self, carte_sur_le_tas):
        
        if carte_sur_le_tas.couleur == self.couleur:
            return True
        # règles aditionelle ici
        elif carte_sur_le_tas.symbole == self.symbole:
            return True
        else:
            return False


    


        