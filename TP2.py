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

    # le joueur essaye de trouver le nombre mystere
    nb_joueur = int(input("Choisissez un nombre:"))

    # boucle qui dit au joueur si le nombre est plus grand, plus petit ou si il a gagné
    if nb_joueur == nb_mystere:
        print("Victoire!")

        # demande au joueur si il veut rejouer et si ce nest pas le cas le code se termine
        rejouer = input("Voulez-vous rejouer? o/n:")

        if rejouer == "o":
            nb_mystere = randint(0,1000)

        elif rejouer == "n":
            print("Au revoir.")
            fin_jeu = True

    elif nb_joueur < nb_mystere:
        print("Le nombre mystere est plus grand.")

    elif nb_joueur > nb_mystere:
        print("Le nombre mystere est plus petit.")
