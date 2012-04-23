#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import dico
import joueur

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

def placer(plateau, mot, position, direction, dictionnaire, chevalet, valeurs):
    """
        place dans le plateau le mot à la position dans la direction
        retourne le nombre de points ou false si on peut pas placer
        retire du chevalet les lettres placées
    """
    lettresSup=verifier(plateau, mot, position, direction, dictionnaire, chevalet)
    if lettresSup==False:
        return False
    x=position[0]
    y=position[1]
    for i in range(len(mot)):
        plateau[x][y]=mot[i]
        x+=direction
        y+=abs(direction-1)
    joueur.retirerChevalet(chevalet, mot, lettresSup) #on enlève du chevalet les lettres placées
    return points(valeurs, mot, position, direction)

def verifier(plateau, mot, position, direction, dictionnaire, chevalet):
    """
        plateau : liste de liste
        mot : string
        position : tuple (x,y)
        direction : 0=horizontal, 1=vertical
        
        Retourne False si on peut pas placer le mot, et les lettres déjà sur la plteau à la place du mot si on peut le placer
    
    """
    lettresSup=compatible(plateau, mot, position, direction)
    if (len(mot)+position[direction] <= 15 and
            joueur.verifierChevalet(chevalet, mot, lettresSup) and
            dico.verifier(mot, dictionnaire) and
            estColle(plateau, mot, position, direction) and
            lettresSup!=False):
        return lettresSup
    return False

def compatible(plateau, mot, position, direction):
    """
        vérifie que le mot puisse être mis par rapport aux autres lettres du jeu
        Retourne les lettres qui sont déjà sur la plateau et qu'on veut utiliser dans le mot
    """
    lettresSup=[]
    j=0
    for i in echantillon(plateau, mot, position, direction):
        if not (i==None or str(i)==mot[j]):
            return False
        if not i==None:
            lettresSup.append(str(i))
        j+=1
    print lettresSup
    return lettresSup

def points(valeurs, mot, position, direction):
    """
        retourne le nombre de points fait par le mot
    """
    points=0
    if len(mot)==7: #Scrabble
        points+=50
    for lettre in mot: #Points des lettres
        points+=int(valeurs[lettre])
    return points

def motsCollateraux(plateau, mot, position, direction, dictionnaire):
    """
        retourne les mots engendrés par le mot placé
    """
    mots=[]
    pos=[]
    pos.extend(position)
    for lettre in mot:
        mots.append(motEngendre(plateau, lettre, position, direction))
        pos[0]+=direction
        pos[1]+=abs(direction-1)
    return mots

def motEngendre(plateau, position, direction):
    """
        pour une position donnée, donne le mot engendré par la pose de la lettre
    """
    pass

def estColle(plateau, mot, position, direction):
    """
        Retourne true si le mot a bien un point de contact avec les lettres en place, ou si c'est le premier tour (position = [7,7])
        Retourne False sinon
    """
    x=position[0]
    y=position[1]
    for lettre in mot:
        if (plateau[x][y] or
            plateau[x+1][y]!=None or
            plateau[x-1][y]!=None or
            plateau[x][y+1]!=None or
            plateau[x][y-1]!=None or
            (position[0]==7 and position[1]==7)):
            return True
        x+=direction
        y+=abs(direction-1)
    return False

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