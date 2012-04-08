#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sac

def init(Sac):
    """
        initialise un joueur (chevalet, points)
    """
    joueur={}
    joueur["chevalet"]=creerChevalet(Sac)
    joueur["points"]=0
    return joueur

def creerChevalet(Sac):
    chevalet=[]
    for i in range(0,7):
        chevalet.append(sac.piocher(Sac))
    return chevalet

def ajouterPoints(n, joueur):
    joueur["points"]+=n

def remplirChevalet(chevalet, Sac):
    """
        remplit le chevalet pour qu'il arrive à 7 lettres
    """
    for i in range(len(chevalet), 7):
        chevalet.append(sac.piocher(Sac))

def retirerChevalet(chevalet, mot):
    """
       Retire le mot du chevalet (attention, d'abord vérifier que mot dans chevalet) 
    """
    for lettre in mot:
        chevalet.remove(lettre)

def verifierChevalet(chevalet, mot):
    """
        vérifie que le mot est bien dans le chevalet
    """
    test=[]
    test.extend(chevalet)
    for lettre in mot:
        if not test.count(lettre)==0:
            test.remove(lettre)
        else:
            return False
    return True