#!/usr/bin/env python
# -*- coding: utf-8 -*-

def afficher(plateau):
    espace = '\t'
    print espace,
    for y in range(0,15):
        print str(y)+espace,
    print ''
    i = 0
    for x in plateau:
        print str(i)+espace,
        i += 1
        for case in x:
            if case == (1,1): #normale
                print '.'+espace,
            elif case == (2,1): #mot double
                print '#2'+espace,
            elif case == (3,1): #mot triple
                print '#3'+espace,
            elif case == (1,2): #lettre double
                print '%2'+espace,
            elif case == (1,3): #lettre triple
                print '%3'+espace, 
            else:
                print str(case)+espace,
        print '\n\n'


def demande(phrase):
    retour=raw_input(phrase)
    if retour==42:
        quit()
    return retour


