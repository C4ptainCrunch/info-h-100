#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import dico
import joueur

def init(multiplicateurs):
    """
    Initialise un plateau de jeu
    
    Arguments :
        multiplicateurs (liste) : liste des cases avec multiplicateur.
            Les deux premiers éléments de la liste représentatent la position
            (x, y), le troisième représente le multiplicateur du mot et le
            dernier le multiplicateur de la lettre.
    
    Valeur de retour : (liste)
        Retourne une liste de listes de tuples. Chaque sous-liste représente une
        ligne du plateau. Dans chaque sous-tuple (a,b), le premier élément (a)
        est le multiplicateur du mot et le second (b) le multiplicateur de la
        lettre.
    """
    plateau = []
    for i in range(0,15):
        ligne=[]
        for j in range(0,15):
            ligne.append((1,1))
        plateau.append(ligne)
    for case in multiplicateurs:
        plateau[int(case[0])][int(case[1])]=(int(case[2]),int(case[3]))
    return plateau

def placer(plateau, mot, position, direction, dictionnaire, chevalet, valeurs):
    """
    Vérifie que le mot peut être posé.
    S'il peut, place dans le plateau le mot donnée à la position donnée dans la
    direction donnée, et retire du chevalet les lettres placées.
    
    Arguments :
        plateau (liste) : Le plateau de jeu
        mot (string) : Le mot à placer sur le plateau
        position (tuple) : position x et y de la première lettre du mot à placer
        direction (int) : 0 si horizontalement, 1 si verticalement
        dictionnaire (tuple) : Chaque élément du tuple est un mot autorisé
        chevalet (liste) : Liste des lettres du chevalet du joueur
        valeurs (dictionnaire) : Associe à chaque lettre le nombre de point
            qu'elle vaut au Scrabble
    
    Valeurs de retour :
        Si le mot ne peut être placé :
            False
        Si le mot peut être placé :
            Points : nombre de points qu'engendre le placement du mot.
    """
    Points=points(plateau,valeurs, mot, position, direction)
    motsCollateraux = findMotsCollateraux(plateau, mot, position, direction)
    lettresSup=verifier(plateau, mot, position,
                        direction, dictionnaire, chevalet,motsCollateraux)
    if lettresSup==False:
        return False
    x=position[0]
    y=position[1]
    for i in range(len(mot)):
        plateau[x][y]=mot[i]
        x+=direction
        y+=abs(direction-1)
    joueur.retirerChevalet(chevalet, mot, lettresSup)
    return Points

def verifier(plateau, mot, position, direction,
             dictionnaire, chevalet,motsCollateraux):
    """
    Vérifie que le mot à placer peut effectivement être placé.
    
    Arguments :
        plateau (liste) : Le plateau de jeu
        mot (string) : Le mot à placer sur le plateau
        position (tuple) : position x et y de la première lettre du mot à placer
        direction (int) : 0 si horizontalement, 1 si verticalement
        dictionnaire (tuple) : Chaque élément du tuple est un mot autorisé
        chevalet (liste) : Liste des lettres du chevalet du joueur
        motsCollateraux (liste) : Liste des mots perpendiculaires engendrés par
            la pose du mot.
    
    Valeurs de retour :
        Si le mot ne peut être placé :
            False
        Si le mot peut être placé :
            lettresExistantes (liste) : liste des lettres déjà présentes sur le
            plateau aux emplacements du nouveau mot.

    """
    lettresSup=compatible(plateau, mot, position, direction)
#    for motCollateral in motsCollateraux:
#        if not dico.verifier(motCollateral, dictionnaire):
#            return False
    if (len(mot)+position[direction] <= 15 and
            joueur.verifierChevalet(chevalet, mot, lettresSup) and
            dico.verifier(mot, dictionnaire) and
            estColle(plateau, mot, position, direction) and
            lettresSup!=False):
        return lettresSup    
    return False

def compatible(plateau, mot, position, direction):
    """
    Vérifie que le mot puisse être mis par rapport aux autres lettres du jeu.
    
    Arguments :
        plateau (liste) : Le plateau de jeu
        mot (string) : Le mot à placer sur le plateau
        position (tuple) : position x et y de la première lettre du mot à placer
        direction (int) : 0 si horizontalement, 1 si verticalement
    
    Valeur de retour : (liste)
        lettresExistantes (liste) : liste des lettres déjà présentes sur le
        plateau aux emplacements du nouveau mot.
    """
    lettresSup=[]
    j=0
    for i in echantillon(plateau, mot, position, direction):
        if not (estVide(i) or str(i)==mot[j]):
            return False
        if not estVide(i):
            lettresSup.append(str(i))
        j+=1
    return lettresSup

def points(plateau, valeurs, mot, position, direction):
    """
    Calcule le nombre de points engendrés par la pose du mot.
    
    Arguments :
        plateau (liste) : Le plateau de jeu
        valeurs (dictionnaire) : Associe à chaque lettre le nombre de point
            qu'elle vaut au Scrabble
        mot (string) : Le mot à placer sur le plateau
        position (tuple) : position x et y de la première lettre du mot à placer
        direction (int) : 0 si horizontalement, 1 si verticalement
    
    Valeur de retour : (int)
        points : nombre de points engendrés par la pose du mot.
    """
    points=0
    multiplicateurMot=1
    x=position[0]
    y=position[1]
    if len(mot)==7: #Scrabble
        points+=50
    for lettre in mot: #Points des lettres
        if estVide(plateau[x][y]):
            points+=int(valeurs[lettre])*plateau[x][y][1]
            multiplicateurMot*=plateau[x][y][0]
        x+=direction
        y+=abs(direction-1)
    points*=multiplicateurMot
    return points

def findMotsCollateraux(plateau, mot, position, direction):
    """
    Trouve les mots perpendiculaires engendrés par la pose du mot.
    
    Arguments :
        plateau (liste) : Le plateau de jeu
        mot (string) : Le mot à placer sur le plateau
        position (tuple) : position x et y de la première lettre du mot à placer
        direction (int) : 0 si horizontalement, 1 si verticalement
    
    Valeur de retour : (liste)
        mots : 
        
    """
    mots=[]
    x=position[0]
    y=position[1]
    for lettre in mot:
        engendre=motEngendre(plateau, lettre, position, direction)
        if len(engendre)>2:
            mots.append(engendre)
        x+=direction
        y+=abs(direction-1)
    return mots

def motEngendre(plateau, lettre, position, direction):
    """
    pour une position donnée, donne le mot engendré par la pose de la lettre
    """
    x=position[0]
    y=position[1]
    lettreActuelle = lettre
    while not estVide(lettreActuelle):
        x-=abs(direction-1)
        y-=direction
        lettreActuelle = plateau[x][y]
    x+=abs(direction-1)
    y+=direction
    lettreActuelle = plateau[x][y]
    motEngendre = ''
    while not estVide(lettreActuelle):
        motEngendre += lettreActuelle
        x+=abs(direction-1)
        y+=direction
        lettreActuelle = plateau[x][y]
    return motEngendre
        
    

def estColle(plateau, mot, position, direction):
    """
    Retourne true si le mot a bien un point de contact avec les lettres en place,
    ou si c'est le premier tour (position = [7,7])
    Retourne False sinon
    """
    x=position[0]
    y=position[1]
    for lettre in mot:
        if (plateau[x][y] or
            (not estVide(plateau[x+1][y])) or
            (not estVide(plateau[x-1][y])) or
            (not estVide(plateau[x][y+1])) or
            (not estVide(plateau[x][y-1])) or
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

def estVide(case):
    return type(case) == type((1,1))
