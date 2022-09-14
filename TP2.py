# Emile Macabies 2022
# Jeu de devinnettes

# importations
from random import *

# definition des variables
nb_mystere = randint(0,1000)
fin_jeu = False
nb_essais = 0
rejouer = None

#boucle qui prends fin lorsque le joueur ne veut plus jouer
while fin_jeu == False:
    nb_essais = nb_essais + 1

    # le joueur essaye de trouver le nombre mystere
    nb_joueur = int(input("Choisissez un nombre:"))

    # boucle qui dit au joueur si le nombre est plus grand, plus petit ou si il a gagné
    if nb_joueur == nb_mystere:
        print("Victoire! Vous avez réussi en", nb_essais, "essais.")

        # demande au joueur si il veut rejouer et si ce nest pas le cas le code se termine
        rejouer = input("Voulez-vous rejouer? o/n:")

        if rejouer == "o":
            nb_mystere = randint(0,1000)
            nb_essais = 0

        elif rejouer == "n":
            print("Au revoir.")
            fin_jeu = True

    elif nb_joueur < nb_mystere:
        print("Le nombre mystere est plus grand que", nb_joueur)

    elif nb_joueur > nb_mystere:
        print("Le nombre mystere est plus petit que", nb_joueur)
