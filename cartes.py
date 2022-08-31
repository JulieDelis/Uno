class Carte:
    def __init__(self, couleur, symbole):
        self.couleur = couleur
        self.symbole = symbole  
    
    def montrer(self):
        """
        Permet de montré le contenue d’instances contenant des carte
        ATENTION cette fonction ne retourne rien, si utiliser avec print, valeur affichée = None
        """
        print((self.couleur, self.symbole))
    # ! cette fonction ne retourne rien, si utliser avec print, valeur affichée = None
    
    def peut_poser(self, carte_sur_le_tas):
        """
        Permet de retourner une valeur booléenne selon si la carte peut être poser 
        """
        if carte_sur_le_tas.couleur == self.couleur:
            return True
        # règles aditionelle ici
        elif carte_sur_le_tas.symbole == self.symbole:
            return True
        else:
            return False


    


        