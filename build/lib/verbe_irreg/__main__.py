#!/usr/bin/python -tt
# -*- coding: utf-8 -*-
import random
import os
from verbe_irreg import games_mode
from verbe_irreg import load_list

def main():
    verbes = {}

    verbes = load_list.load_list()
    
    while True:
    
    
        rand = random.SystemRandom().choice(list(verbes.items()))
        verb, (pret, past, trad) = rand
        # print "Le verbe %s se conjugue au prétérit par %s, au participe passé par %s et se traduit par %s" % (verb, pret, past, trad)
        lst = []
        lst.append(verb)
        lst.append(pret)
        lst.append(past)
        lst.append(trad)
    
        print("""\nDeux modes de jeu sont proposés :
    
        \t soit le programme va afficher le verbe irrégulier à l'infinitif et vous
        \tdevrez trouver son prétérit, son participe passé et sa traduction en Français.
        """)
    
        print("Par exemple : si le verbe '%s' est proposé, il faudra répondre '%s', '%s' et '%s'" %(lst[3], lst[0], lst[1], lst[2]))
    
        print("""
        \t soit le programme va afficher la traduction du verbe en Français et vous 
        \t devrez dans ce cas la, trouver son infinitif, son prétérite et son participe passé.
        """)
    
        print("Par exemple : si le verbe '%s' est proposé, il faudra répondre '%s', '%s' et '%s'" %(lst[0], lst[1], lst[2], lst[3]))
        print("\n")
    
    
        jeu = input("""\t Si vous souhaitez jouer avec l'infinitif du verbe merci de tapper 1
         Si vous souhaitez jouer avec la traduction Française du verbe merci de tapper 2  
         Si vous souhaitez changer de liste tapper 3
         Si vous souhaitez quitter tapper 4
         >>> """)
    
        if jeu == "1":
            numb = input("\t Combien de fois souhaitez vous faire la liste ? >>>  ")
            numb = int(numb)
            games_mode.infinitif(numb,verbes)
        elif jeu == "2":
            numb = input("\t Combien de fois souhaitez vous faire la liste ? >>>  ")
            numb = int(numb)
            games_mode.traduction(numb,verbes)
        elif jeu == "3":
            verbes = load_list.load_list()
        elif jeu == "4":
            break



if __name__ == "__main__":
    main()