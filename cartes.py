class Carte:
    def __init__(self, couleur, symbole):
        self.couleur = couleur
        self.symbole = symbole  
    
    def montrer(self):
        print((self.couleur, self.symbole))

    
    def peut_poser(self, carte_sur_le_tas):
        
        if carte_sur_le_tas.couleur == self.couleur:
            return True
        # règles aditionelle ici
        elif carte_sur_le_tas.symbole == self.symbole:
            return True
        else:
            return False


    


        