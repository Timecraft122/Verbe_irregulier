import random
import os

def infinitif(numb,verbes):
    counter = 0
    score = 0
    tour_de_liste = 0
    total_counter = 0
    list_random=list(verbes.items())

    random.shuffle(list_random)

    while tour_de_liste < numb :

        verb, (pret, past, trad) = list_random[counter]
        lst = []
        lst.append(verb)
        lst.append(pret)
        lst.append(past)
        lst.append(trad)

        print("Le verbe à l'infinitif est le suivant '%s'" % (lst[0]))

        reponsepret = input("Quel est son prétérit? >>> ")
        if reponsepret == lst[1]:
            print("\033[32m Bravo bien joué!\033[0m")
            score = score + 1
        else:
            print("\033[31m Mauvaise réponse")
            print("\033[31m La bonne réponse est '%s'\033[0m" % lst[1])

        reponsepp = input("Quel est son participe passé? >>> ")
        if reponsepp == lst[2]:
            print("\033[32m Bravo bien joué!\033[0m")
            score = score + 1
        else:
            print("\033[31m Mauvaise réponse")
            print("\033[31m La bonne réponse est '%s'\033[0m" % lst[2])

        reponsetrad = input("Quel est sa traduction Française? >>> \033[0m")
        if reponsetrad == lst[3]:
            print("\033[32m Bravo bien joué!\033[0m")
            score = score + 1
        else:
            print("\033[31m Mauvaise réponse")
            print("\033[31m La bonne réponse est '%s'\033[0m" % lst[3])

        counter += 1
        total_counter += 1
        if len(list_random) == counter :
            tour_de_liste += 1
            random.shuffle(list_random)
            counter=0
        print(ratio(score, total_counter))


def traduction(numb, verbes):
    

    counter = 0
    score = 0
    tour_de_liste = 0
    total_counter = 0
    list_random=list(verbes.items())

    random.shuffle(list_random)

    while tour_de_liste < numb :

        verb, (pret, past, trad) = list_random[counter]
        lst = []
        lst.append(verb)
        lst.append(pret)
        lst.append(past)
        lst.append(trad)

        print("La traduction Française est la suivante '%s'" % (lst[3]))

        reponseinf = input("Quel est son infinitif en Anglais? >>> ")
        if reponseinf == lst[0]:
            print("\033[32m Bravo bien joué!\033[0m")
            score = score + 1
        else:
            print("\033[31m Mauvaise réponse")
            print("\033[31m La bonne réponse est '%s'\033[0m" % lst[0])

        reponsepret = input("Quel est son prétérit? >>> ")
        if reponsepret == lst[1]:
            print("\033[32m Bravo bien joué!\033[0m")
            score = score + 1
        else:
            print("\033[31m Mauvaise réponse")
            print("\033[31m La bonne réponse est '%s'\033[0m" % lst[1])

        reponsepp = input("Quel est son participe passé? >>> ")
        if reponsepp == lst[2]:
            print("\033[32m Bravo bien joué!\033[0m")
            score = score + 1
        else:
            print("\033[31m Mauvaise réponse")
            print("\033[31m La bonne réponse est '%s'\033[0m" % lst[2])

        counter += 1
        total_counter += 1
        if len(list_random) == counter :
            tour_de_liste += 1
            random.shuffle(list_random)
            counter = 0
        print(ratio(score, total_counter))

def ratio(score, counter):
    return("Vous avez %d réponses de juste sur %d") % (score, (counter*3))