import cartes
import random


def printN(text) :
    Retoure_a_la_ligne = "\n"
    print(Retoure_a_la_ligne, text)

def genere_cartes(couleurs, symboles, nb_joueurs):
    jeu = []
    nb_jeu = nb_joueurs * 7 + nb_joueurs + 1 # 1 pour le tas et une carte de pioche chaque joueur
    for joueur in range(nb_joueurs % 40): # 40 ou nombre de cartes dans un jeu
        for couleur in couleurs:
            for symbole in symboles:
            # ici pour symbole dans feneration if symbol == id du symbol mettre 2 cartes de ça
                carte = cartes.Carte(couleur, symbole)
                jeu.append(carte)
    return jeu


def melange(pioche):
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
     # liste de liste instance pour pioche, tas , joueurs
    """ Retourne une liste d'instances de jeu contenant les cartes dans l'ordre suivant, joueurs, pioche, tas."""
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
    couleurs = ["bleu", "rouge", "jaune", "vert"]
    symboles = range(10)

    instances = distribue(melange(genere_cartes(couleurs, symboles, nb_joueurs)), nb_joueurs)
    return instances

def joue(joueur, pioche, tas): # un joueur = liste de cartes = cartes ici
    cartes_jouables = [] # indices des cartes
    #printN("---------------")
    #print("carte de joueur : ")
    for carte in joueur:
        carte.montrer()
    #printN("-----")
    for carte_id, carte in enumerate(joueur):
        # print(tas[-1].montrer())
        if carte.peut_poser(tas[-1]):
            cartes_jouables.append(carte_id)
    # print(cartes_jouables)
    printN("Le tas est : ")
    tas[-1].montrer()
    if cartes_jouables == []:
        joueur.append(pioche.pop(0))
    else:
        carte_id = cartes_jouables[random.randint(0, len(cartes_jouables)-1)]
        printN("Le joueur joue la carte : ")  
        joueur[carte_id].montrer()
        tas.append(joueur.pop(carte_id))
    #printN("-----")
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
            print("\n","carte du joueur numéro : ", num + 1)
            if joueur == []:
                print(num, "gagné")
                fin_du_jeu = True
                break
            joueur, pioche, tas = joue(joueur, pioche, tas)