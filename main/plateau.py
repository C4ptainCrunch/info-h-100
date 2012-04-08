#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import dico
import joueur

def verifier(plateau, mot, position, direction, dictionnaire, chevalet):
    """
        plateau : liste de liste
        mot : string
        position : tuple (x,y)
        direction : 0=horizontal, 1=vertical
    
    """
    return (len(mot)+position[direction] <= 15 and
            joueur.verifierChevalet(chevalet, mot) and
            dico.verifier(mot, dictionnaire) and
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

def placer(plateau, mot, position, direction, dictionnaire, chevalet):
    """
        place dans le plateau le mot à la position dans la direction
    """
    if not verifier(plateau, mot, position, direction, dictionnaire, chevalet):
        return False
    x=position[0]
    y=position[1]
    for i in range(len(mot)):
        plateau[x][y]=mot[i]
        x+=direction
        y+=abs(direction-1)
    return True

def init():
    """
        Initialise le plateau avec uniquement des None
    """
    plateau = []
    for i in range(0,15):
        ligne=[]
        for j in range(0,15):
            ligne.append(None)
        plateau.append(ligne)
    return plateau