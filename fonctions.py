import cartes
import random

def genere_cartes(couleurs, symboles, nb_joueurs):

    """ Génère les cartes.
    arguments:
        couleurs: liste des couleurs attribuées aux cartes, servira dans la génération, la fonctions génère un certains nombre n de cartes pour chaque couleur.
        symboles: liste des symboles qui doivent apparaitre sur les cartes, pour l'insant on attend la liste des nombres de 0 à 9 (compris) mais cela sera ammené à changer avec l'ajout de nouveaux
        symboles.
        nb_joueurs: nombre de joueur qui influence le nombre de paquets généré, si le nombre de joueur est trop élévé alors la fonction générera un paquet de cartes en plus

    Cette fonctions retourne une liste d'objets cartes dans leur ordre de génération.
        """
    
    jeu = []
    nb_jeu = nb_joueurs * 7 + nb_joueurs + 1 # 1 pour le tas et une carte de pioche chaque joueur
    for joueur in range(nb_joueurs % 40): # 40 ou nombre de cartes dans un jeu
        for couleur in couleurs:
            for symbole in symboles:
            # ici pour symbole dans generation if symbol == id du symbol mettre 2 cartes de ça
                carte = cartes.Carte(couleur, symbole)
                jeu.append(carte)
    return jeu


def melange(pioche):

    """Mélange les éléments de la liste donnée en argument, retourne une nouvelle liste."""

    indices_deja_passe = []
    nouvelle_pioche = []
    while len(nouvelle_pioche) < len(pioche):

        indice_aleatoire = random.randint(0, len(pioche)-1)

        if indice_aleatoire in indices_deja_passe:
            continue

        nouvelle_pioche.append(pioche[indice_aleatoire])
        indices_deja_passe.append(indice_aleatoire)
    return nouvelle_pioche



def distribue(cartes, nb_joueur):

    """Attribue les cartes d'une liste à trois instances: la piohce, le tas, et les joueurs.
arguments:
    cartes: liste des cartes à distribuer entre les trois instances
    nb_joueur: nombre de joueur auquels on devra attribuer chacun 7 cartes
Retourne une liste d'instances de jeu, c'est à dire de listes, contenant les cartes dans l'ordre suivant, joueurs, pioche, tas."""

    pioche = cartes
    tas = [pioche.pop(0)]
    # s'assurer que on tape pas 1
    instances = []
    for i in range(nb_joueur):
        joueur = []
        for nb_carte in range(7):
            joueur.append(pioche.pop(0))
        instances.append(joueur)
    instances.append(pioche)
    instances.append(tas)
    
    return instances



def preparation(nb_joueurs):

    """ Prépare le jeu le paquets de cartes pour le début du jeu.
    arguments: 
        nb_joueurs: nombre de joueurs (pour l'instant il n'est question de bots) 
    Retourne une liste de listes (instances de jeu) d'objets carte."""

    couleurs = ["bleu", "rouge", "jaune", "vert"]
    symboles = range(10)

    instances = distribue(melange(genere_cartes(couleurs, symboles, nb_joueurs)), nb_joueurs)
    return instances

def joue(joueur, pioche, tas):
    
    """ Joue pour un bot.
    arguments: 
        joueur: liste des cartes d'un joueur
        pioche: liste ordonnée des cartes contenus dans la pioche au moment du tour du joueur
        tas: carte sur le tas au moment du tour du joueur
    Retourne une nouvelle instance de chacun des arguments (c-à-d une nouvelle liste de cartes) en fonction des modifications faites au cour du tour du joueur."""
    
     # un joueur = liste de cartes = cartes ici
    cartes_jouables = [] # indices des cartes
    coulleur_de_baze = '\033[0m' # Défini la couleur en blanc sinon la couleur des textes continue d’être de la couleur de la dernière carte  
    print(coulleur_de_baze, "---------------")
    print("carte de joueur : ")
    for carte in joueur:
        carte.montrer()
    print(coulleur_de_baze,"-----")
    for carte_id, carte in enumerate(joueur):
        # print(tas[-1].montrer())
        if carte.peut_poser(tas[-1]):
            cartes_jouables.append(carte_id)
    # print(cartes_jouables)
    print(coulleur_de_baze, "Le tas est : ")
    tas[-1].montrer()
    if cartes_jouables == []:
        joueur.append(pioche.pop(0))
    else:
        carte_id = cartes_jouables[random.randint(0, len(cartes_jouables)-1)]
        print(coulleur_de_baze, "Le joueur joue la carte : ")  
        joueur[carte_id].montrer()
        tas.append(joueur.pop(carte_id))
    print(coulleur_de_baze, "-----")
    return joueur, pioche, tas


def pioche_vide(pioche, tas):
    if pioche == []:
        nouvelle_pioche = melange(tas[:-1])
        nouveau_tas = tas[0]
        return nouvelle_pioche, [nouveau_tas]
    else:
        return False


def jeu():
    nb_joueurs = int(input("Donnez le nombre de joueur :"))
    instances = preparation(nb_joueurs)
    joueurs = instances[:-2]
    pioche = instances[-2]
    tas = instances[-1]
    fin_du_jeu = False
    while not fin_du_jeu:
        for num, joueur in enumerate(joueurs):
            if pioche_vide(pioche, tas):
                pioche, tas = pioche_vide(pioche, tas)
            print("joueur numéro : ", num + 1)
            if joueur == []:
                print(num, "gagné")
                fin_du_jeu = True
                break
            joueur, pioche, tas = joue(joueur, pioche, tas)