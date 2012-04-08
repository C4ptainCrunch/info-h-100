#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def plateau():
    plateau=[]
    ligne=range(0,15)
    for i in range(0,15):
        plateau.append(ligne)
    return plateau

plateau=plateau()

def verifier(plateau, mot, position, direction):
    """
        plateau : liste de liste
        mot : string
        position : tuple (x,y)
        direction : 0=x, 1=y
    
    """
    return (len(mot)+position[direction] <= 15 and
            joueur.verifier(mot) and
            dico.verifier(mot) and
            compatible(plateau, mot, position, direction))

def echantillon(plateau, mot, position, direction):
    """
        retourne le "mot" qui est en lieu et place de ce que le user veut placer
    """
    echantillon=[]
    x=position[0]
    y=position[1]
    for i in range(len(mot)):
        echantillon.append(plateau[x][y])
        x+=direction
        y+=abs(direction-1)
    return echantillon

def compatible(plateau, mot, position, direction):
    """
        vérifie que le mot puisse être mis par rapport aux autres lettres du jeu
    """
    j=0
    for i in echantillon(plateau, mot, position, direction):
        if not (i==None or str(i)==mot[j]):
            return False
        j+=1
    return True