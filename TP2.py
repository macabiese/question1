# Emile Macabies 2022
# Jeu de devinnettes

# importations
from random import *

borne_min = int(input("Rentrez la borne minimale:_"))
borne_max = int(input("Rentrez la borne maximale:_"))

def jeu():

    # definition des variables
    fin_jeu = False
    nb_mystere = randint(borne_min, borne_max)
    rejouer = None
    nb_essais = 0

    #boucle qui prends fin lorsque le joueur ne veut plus jouer
    while fin_jeu == False:
        nb_essais = nb_essais + 1

        # Introduction au jeu
        if nb_essais <= 1:
            print("J’ai choisi un nombre au hasard entre", borne_min, "et ", borne_max,". À vous de le deviner...")

        # le joueur essaye de trouver le nombre mystere
        nb_joueur = int(input("Entrez votre essai :_"))

        # boucle qui dit au joueur si le nombre est plus grand, plus petit ou si il a gagné
        if nb_joueur == nb_mystere:
            print("Bravo! Bonne réponse.\nVous avez réussi en :", nb_essais,"essai(s).")

            # demande au joueur si il veut rejouer et si ce nest pas le cas le code se termine
            rejouer = input("Voulez-vous faire une autre partie (o/n)? _")

            if rejouer == "o":
                nb_mystere = randint(0,1000)
                nb_essais = 0

            elif rejouer == "n":
                print("Merci et au revoir...")
                fin_jeu = True

        elif nb_joueur < nb_mystere:
            print("Mauvais choix, le nombre est plus grand que", nb_joueur)

        elif nb_joueur > nb_mystere:
            print("Mauvais choix, le nombre est plus petit que", nb_joueur)

jeu()