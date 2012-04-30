#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POUR LES EXEMPLES DES FONCTIONS, VOIR :
"doc/examples/nomdumodule/nomdelafonction.ex"
"""

import random

def init(lettres):
    """
    Initialise un sac
    
    Arguments :
        lettres (list) : Liste des lettres, du nombre qu'il y en a et du nombre
            de points qu'elles vallent pour le jeu de Scrabble.
    
    Valeur de retour : (list)
        Retourne une liste de lettres (String)
    """
    sac=[]
    for lettre in lettres:
        n=int(lettre[1])
        for i in range(n):
            sac.append(lettre[0])
    return sac

def piocher(sac):
    """
    Pioche une lettre dans le sac, et la retire de celui-ci
    
    Arguments :
        Sac (list) : liste de lettres (String)
    
    Valeur de retour : (String)
        Retourne la lettre piochée.
    """
    if len(sac)!=0:
        i=random.randint(0,len(sac)-1)
        return sac.pop(i)