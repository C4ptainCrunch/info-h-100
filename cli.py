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
            if type(case) == type((None,)):
                print '+'+espace,
            else:
                print str(case)+espace,
        print '\n\n'


def demande(phrase):
    retour=raw_input(phrase)
    if retour==42:
        quit()
    return retour

