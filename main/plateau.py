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

def motsCollateraux(plateau, mot, position, direction, dictionnaire):
    """
        retourne les mots engendrés par le mot placé
    """
    mots=[]
    pos=[]
    pos.extend(position)
    for lettre in mot:
        mots.append(motEngendre(ARG))
        pos[0]+=direction
        pos[1]+=abs(direction-1)
    return mots

def motEngendre(plateau, position, direction):
    """
        pour une position donnée, donne le mot engendré par la pose de la lettre
    """
    pass
    

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

def placer(plateau, mot, position, direction, dictionnaire, chevalet, valeurs):
    """
        place dans le plateau le mot à la position dans la direction
        retourne le nombre de points ou false si on peut pas placer
        retire du chevalet les lettres placées
    """
    if not verifier(plateau, mot, position, direction, dictionnaire, chevalet):
        return False
    x=position[0]
    y=position[1]
    for i in range(len(mot)):
        plateau[x][y]=mot[i]
        x+=direction
        y+=abs(direction-1)
    joueur.retirerChevalet(chevalet, mot) #on enlève du chevalet les lettres placées
    return points(valeurs, mot, position, direction)

def points(valeurs, mot, position, direction):
    """
        retourne le nombre de points fait par le mot
    """
    points=0
    if len(mot)==7:
        points+=50
    for lettre in mot:
        points+=int(valeurs[lettre])
    return points
        

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