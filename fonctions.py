import cartes
import random

def genere_cartes(couleurs, symboles):
    jeu = []
    for couleur in couleurs:
        for symbole in symboles:
            # ici pour symbole dans feneration if symbol == id du symbol mettre 2 cartes de ça
            carte = cartes.Carte(couleur, symbole)
            jeu.append(carte)
    return jeu


def melange(pioche):
    indices_deja_passe = []
    nouvelle_pioche = []
    while len(nouvelle_pioche) < 40:

        indice_aleatoire = random.randint(0, 39)

        if indice_aleatoire in indices_deja_passe:
            continue

        nouvelle_pioche.append(pioche[indice_aleatoire])
        indices_deja_passe.append(indice_aleatoire)
    return nouvelle_pioche

def distribue(cartes):
     # liste de liste instance pour pioche, tas , joueurs
    """ Retourne une liste d'instances de jeu contenant les cartes dans l'ordre suivant, joueurs, pioche, tas."""
    pioche = cartes
    tas = [pioche.pop(0)]
    nb_joueur = 2 #input("Donnez le nombre de joueur :")
    instances = []
    for i in range(nb_joueur):
        joueur = []
        for nb_carte in range(7):
            joueur.append(pioche.pop(0))
        instances.append(joueur)
    instances.append(pioche)
    instances.append(tas)
    
    return instances

def preparation():
    couleurs = ["bleu", "rouge", "jaune", "vert"]
    symboles = range(10)
    instances = distribue(melange(genere_cartes(couleurs, symboles)))
    return instances

def joue(joueur, pioche, tas): # un joueur = liste de cartes = cartes ici
    cartes_jouables = [] # indices des cartes
    print("carte de joueur : ")
    for carte in joueur:
        carte.montrer()
    print("---------------")
    for carte_id, carte in enumerate(joueur):
        # print(tas[-1].montrer())
        if carte.peut_poser(tas[-1]):
            cartes_jouables.append(carte_id)
    # print(cartes_jouables)
    if cartes_jouables == []:
        joueur.append(pioche.pop(0))
    else:
        carte_id = cartes_jouables[random.randint(0, len(cartes_jouables)-1)]
        #print("Le joueur joue la carte : ")  
        #joueur[carte_id].montrer()
        tas.append(joueur.pop(carte_id))

    return joueur, pioche, tas

def jeu():
    instances = preparation()
    joueurs = instances[:-2]
    pioche = instances[-2]
    tas = instances[-1]
    fin_du_jeu = False
    while not fin_du_jeu:
        for num, joueur in enumerate(joueurs):
            for carte_du_tas in tas[-2:]:
             carte_du_tas.montrer()
            print("joueur numéro : ", num)
            if joueur == []:
                print(num, "gagné")
                fin_du_jeu = True
                break
            joueur, pioche, tas = joue(joueur, pioche, tas)