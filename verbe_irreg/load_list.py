import random
import os

def load_list():
    verbes = {}

    found_file=False

    while found_file != True :

        n = input("""\t Quel liste veut tu apprendre ? (taper "all" pour toute)
        \t >>>""")

        if n == "all" :
            found_file = os.path.exists("data/liste_1.txt")
        else :
            found_file = os.path.exists("data/liste_%s.txt"%(n))
        
        if found_file == False :
            print("Ce fichier n'éxiste pas !")

    if n == "all" :
        n = 1
        while found_file == True :
            liste = open("data/liste_%s.txt"%(n), 'r')
            for line in liste:
                line = line.strip()
                verb_split = line.split(' ')
                inf = verb_split[0]
                pret = verb_split[1]
                past = verb_split[2]
                trad = verb_split[3]
                verbes[inf] = [pret,past,trad]
            n += 1
            found_file = os.path.exists("data/liste_%s.txt"%(n))
    else :
        liste = open("data/liste_%s.txt"%(n), 'r')
        for line in liste:
            line = line.strip()
            verb_split = line.split(' ')
            inf = verb_split[0]
            pret = verb_split[1]
            past = verb_split[2]
            trad = verb_split[3]
            verbes[inf] = [pret,past,trad]

    return(verbes)
