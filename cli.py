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
    retour=raw_input(phrase+' ')
    if retour==42:
        quit()
    return retour

def info(phrase):
    print phrase

def afficherChevalet(chevalet):
    print 'Chevalet :',
    for lettre in chevalet:
        print lettre + ' ',
    print ''

def demanderJoueur():
    nb = 0
    while not (0 < nb < 5):
        nb = demande('Nombre de joueurs ?')
        if nb.isdigit():
            nb = int(nb)
    return nb

def demanderJeter():
    delete = '%'
    while not (len(delete) == 1 and delete.isalpha()):
        delete = demande('Quelle lettre voulez vous jeter ?')
        if delete.isalpha():
            delete = delete.upper()
    return delete

def demanderMot():
    mot = demande('Quel mot voulez-vous former ?')
    return (False if mot is '' else mot.upper())

def demanderCoord(sens):
    coord = -1
    while not (0 <= coord <= 14):
        coord = demande('Numéro de '+sens+' ?')
        if coord.isdigit():
            coord = int(coord)
    return coord

def demanderDirection():
    sens = -1
    while not (sens == 1 or sens == 0):
        sens = demande('Dans quel sens voulez-vous placer le mot ? (0 = horizontal, 1 = vertical)')
        if sens.isdigit():
            sens = int(sens)
    return sens

    
