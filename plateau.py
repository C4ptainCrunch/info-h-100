#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""
POUR LES EXEMPLES DES FONCTIONS, VOIR :
"doc/examples/nomdumodule/nomdelafonction.ex"
"""

import dico
import joueur

def init(multiplicateurs):
    """
    Initialise un plateau de jeu
    
    Arguments :
        multiplicateurs (list) : liste des cases avec multiplicateur.
            Chaque multiplicateur est repérsenté par une liste (len(liste)==4)
            Les deux premiers éléments de la liste représentatent la position
            (x, y), le troisième représente le multiplicateur du mot et le
            dernier le multiplicateur de la lettre.
    
    Valeur de retour : (list)
        Retourne une liste de listes (matrice) de tuples.
        Chaque sous-liste représente une ligne du plateau.
        Dans chaque sous-tuple (a,b), le premier élément (a)
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
        plateau (list) : Le plateau de jeu
        mot (string) : Le mot en majuscules à placer sur le plateau
        position (tuple) : position x et y de la première lettre du mot à placer
        direction (int) : 0 si horizontalement, 1 si verticalement
        dictionnaire (tuple) : Chaque élément du tuple est un mot autorisé
        chevalet (list) : Liste des lettres du chevalet du joueur
        valeurs (dictionary) : Associe à chaque lettre le nombre de point
            qu'elle vaut au Scrabble
    
    Valeurs de retour :
        Si le mot ne peut être placé :
            False
        Si le mot peut être placé :
            Points : nombre de points qu'engendre le placement du mot.
    """
    motsCollateraux = trouverMotsCollateraux(plateau, mot, position, direction)
    Points=points(plateau,valeurs, mot, position, direction, motsCollateraux)
    lettresExistantes=verifier(plateau, mot, position,
                        direction, dictionnaire, chevalet,motsCollateraux)
    if lettresExistantes==False:
        return False
    x=position[0]
    y=position[1]
    for i in range(len(mot)):
        plateau[x][y]=mot[i]
        x+=direction
        y+=abs(direction-1)
    joueur.retirerChevalet(chevalet, mot, lettresExistantes)
    return Points

def verifier(plateau, mot, position, direction,
             dictionnaire, chevalet,motsCollateraux):
    """
    Vérifie que le mot à placer peut effectivement être placé.
    
    Arguments :
        plateau (list) : Le plateau de jeu
        mot (string) : Le mot à placer sur le plateau
        position (tuple) : position x et y de la première lettre du mot à placer
        direction (int) : 0 si horizontalement, 1 si verticalement
        dictionnaire (tuple) : Chaque élément du tuple est un mot autorisé
        chevalet (list) : Liste des lettres du chevalet du joueur
        motsCollateraux (list) : Liste des mots perpendiculaires engendrés par
            la pose du mot.
    
    Valeurs de retour :
        Si le mot ne peut être placé :
            False
        Si le mot peut être placé :
            lettresExistantes (list) : liste des lettres déjà présentes sur le
            plateau aux emplacements du nouveau mot.

    """
    lettresExistantes=compatible(plateau, mot, position, direction)
    for motCollateral in motsCollateraux:
        if not dico.verifier(motCollateral[0], dictionnaire):
            return False
    if (len(mot)+position[direction] <= 15 and
            joueur.verifierChevalet(chevalet, mot, lettresExistantes) and
            dico.verifier(mot, dictionnaire) and
            estColle(plateau, mot, position, direction) and
            lettresExistantes!=False):
        return lettresExistantes
    return False

def compatible(plateau, mot, position, direction):
    """
    Vérifie que le mot puisse être mis par rapport aux autres lettres du jeu.
    
    Arguments :
        plateau (list) : Le plateau de jeu
        mot (string) : Le mot à placer sur le plateau
        position (tuple) : position x et y de la première lettre du mot à placer
        direction (int) : 0 si horizontalement, 1 si verticalement
    
    Valeur de retour : (list)
        lettresExistantes (list) : liste des lettres déjà présentes sur le
        plateau aux emplacements du nouveau mot.
    """
    lettresExistantes=[]
    j=0
    for i in echantillon(plateau, mot, position, direction):
        if not (estVide(i) or str(i)==mot[j]):
            return False
        if not estVide(i):
            lettresExistantes.append(str(i))
        j+=1
    return lettresExistantes

def points(plateau, valeurs, mot, position, direction, motsCollateraux):
    """
        Calcule le nombre de points engendrés par la pose du mot et des mots
        perpendiculaires.
    """
    points=0
    mots=[[mot, position, direction, False, True]]
    if len(motsCollateraux)>0:
        mots.extend(motsCollateraux)
    for i in mots:
        if i[4]==True: # Si c'est un mot formé
            points+=pointsMot(plateau, valeurs, i[0], i[1], i[2], i[3])
    return points
    

def pointsMot(plateau, valeurs, mot, position, direction, estCollateral):
    """
    Calcule le nombre de points engendrés par la pose du mot.
    
    Arguments :
        plateau (list) : Le plateau de jeu
        valeurs (dictionary) : Associe à chaque lettre le nombre de point
            qu'elle vaut au Scrabble
        mot (string) : Le mot à placer sur le plateau
        position (tuple) : position x et y de la première lettre du mot à placer
        direction (int) : 0 si horizontalement, 1 si verticalement
        estCollateral (bool) : True si mot posé par l'utilisateur
            (pour le "Scrabble")
    
    Valeur de retour : (int)
        points : nombre de points engendrés par la pose du mot.
    """
    points=0
    multiplicateurMot=1
    x=position[0] #position de la première lettre
    y=position[1]
    if len(mot)==7 and not estCollateral: #Scrabble
        points+=50
    for lettre in mot: #Points des lettres
        if estVide(plateau[x][y]):
            points+=int(valeurs[lettre])*plateau[x][y][1]
            multiplicateurMot*=plateau[x][y][0]
        else:
            points+=int(valeurs[lettre])
        x+=direction
        y+=abs(direction-1)
    points*=multiplicateurMot
    return points

def trouverMotsCollateraux(plateau, mot, position, direction):
    """
    Trouve les mots perpendiculaires engendrés par la pose du mot.
    
    Arguments :
        plateau (list) : Le plateau de jeu
        mot (string) : Le mot à placer sur le plateau
        position (tuple) : position x et y de la première lettre du mot à placer
        direction (int) : 0 si horizontalement, 1 si verticalement
    
    Valeur de retour : (list)
        mots : Liste des mots perpendiculaires engendrés par la pose du mot.
        
    """
    mots=[]
    x=position[0]
    y=position[1]
    for lettre in mot: #On parcourt le plateau aux futurs emplacements du mot
        engendre=motEngendre(plateau, lettre, (x,y), direction)
        if estVide(plateau[x][y]): #Si on génère un nouveau mot
            engendre.append(True) #On ajoute True aux éléments du mot engendré
        else:#Si engendre se base sur une lettre existante
            engendre.append(False) #On ajoute False aux éléments du mot engendré
        if len(engendre[0])>1:
            mots.append(engendre)
        x+=direction
        y+=abs(direction-1)
    return mots

def motEngendre(plateau, lettre, position, direction):
    """
    Pour une position donnée, donne le mot engendré perpendiculairement par la
    du mot, pour la lettre donnée.
    
    Arguments :
        plateau (list) : Le plateau de jeu
        lettre (string) : Lettre qu'on place
        position (tuple) : position x et y de la lettre
        direction (int) : 0 si mot à placer horizontalement, 1 si verticalement
    
    Valeur de retour : (list)
        motEngendre : retourne le mot engendré perpendiculairement par la pose
            du mot, pour la lettre donnée, avec sa position de début et sa
            direction
        
    """
    x=position[0]
    y=position[1]
    temp = plateau[x][y] #On garde en mémoire ce qui se trouve sur la case
    plateau[x][y] = lettre #On remplit provisoirement la case
    lettreActuelle = plateau[x][y]
    while not estVide(lettreActuelle): #On boucle vers la gauche ou le haut
    # (dépendant que le mot est placé verticalement ou horizontalement, 
    # respectivement), jusqu'à ce qu'on tombe sur une case vide.
        x-=abs(direction-1)
        y-=direction
        lettreActuelle = plateau[x][y]
    x+=abs(direction-1) #On repars de la dernière case non vide 
    y+=direction
    pos=(x,y)
    dir=abs(direction-1)
    lettreActuelle = plateau[x][y]
    motEngendre = ''
    while not estVide(lettreActuelle): #On boucle vers la droite ou le bas, 
    # jusqu'à tomber sur une case vide, en notant chaque lettre
        motEngendre += lettreActuelle
        x+=abs(direction-1)
        y+=direction
        lettreActuelle = plateau[x][y]
    #On redonne à la case sa valeur initiale
    plateau[position[0]][position[1]] = temp
    return [motEngendre, pos, dir, True] # True signifie estCollateral
        
    

def estColle(plateau, mot, position, direction):
    """
    Vérifie que le mot à placer a bien un point de contact avec les lettres
    présentes sur le plateau.
    
    Arguments :
        plateau (list) : Le plateau de jeu
        mot (string) : Le mot à placer sur le plateau
        position (tuple) : position x et y de la première lettre du mot à placer
        direction (int) : 0 si horizontalement, 1 si verticalement
    
    Valeurs de retour :
        Si le mot a un point de contact ou que c'est le premier tour (en [7,7]):
            True
        Si le mot n'a pas de point de contact et que ce n'est pas en [7,7]:
            False
    """
    x=position[0]
    y=position[1]
    for lettre in mot:
        if (not estVide(plateau[x][y]) or
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
    Trouve le "mot" qui est en lieu et place de ce que l'utilisateur veut placer
    C'est à dire l'ensemble de lettre et de cases vides qui se trouve sur le
    plateau, là où l'utilisateur veut placer son mot.
    
    Arguments :
        plateau (list) : Le plateau de jeu
        mot (string) : Le mot à placer sur le plateau
        position (tuple) : position x et y de la première lettre du mot à placer
        direction (int) : 0 si horizontalement, 1 si verticalement
    
    Valeur de retour : (list)
        echantillon : ensemble de lettre et de cases vides qui se trouve sur le
            plateau, là où l'utilisateur veut placer son mot
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
    """
    Vérifie qu'une case est vide. (et donc que l'argument est une liste)
    
    Arguments :
        case (list ou string) : valeur de la case (liste si vide)
    
    Valeur de retour :
        Si l'argument est une liste :
            True
        Si l'argument n'est pas une liste :
            False
    """
    return type(case) == type((1,1))