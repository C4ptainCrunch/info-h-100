#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sac

def init(Sac):
"""
    initialise un joueur [chevalet, points] sous forme de liste
"""
    joueur=[]
    joueur.append(creerChevalet(Sac))
    joueur.append(0)
    return joueur

def creerChevalet(Sac):
    chevalet=[]
    for i in range(0,7):
        chevalet.append(sac.piocher(Sac))
    return chevalet

def ajouterPoints(n, joueur):
    joueur[1]+=n

def remplirChevalet(chevalet, Sac):
"""
    remplit le chevalet pour qu'il arrive à 7 lettres
"""
    for i in range(len(chevalet), 7):
        chevalet.append(sac.piocher(Sac))

def retirerChevalet(chevalet, mot, lettresSup):
"""
   Retire le mot du chevalet (attention, d'abord vérifier que mot dans chevalet) sans retirer les lettres (lettresSup) qui sont déjà sur le plateau
"""
    temp=lettresSup+chevalet # Magouille par rapport à l'attribution des variables...
    #Seul moyen de "extend" par l'avant de la liste
    for lettre in mot:
        temp.remove(lettre)
    del(chevalet[:])
    chevalet.extend(temp)

def verifierChevalet(chevalet, mot, lettresSup):
"""
vérifie que le mot est bien dans le chevalet (en comptant les lettres déjà sur le plateau)
"""
    test=[] # Si lettresSup=False, on veut retourner False et donc rentrer dans la condition de la liste vide (dans la condition ci dessous)
    if not lettresSup==False:
        test+=lettresSup+chevalet
    for lettre in mot:
        if not test.count(lettre)==0:
            test.remove(lettre)
        else:
            return False
    return True

def gagnant(joueurs):
    """
        Depuis la liste des joueurs, retourne l'indice du joueur qui le plus de points
    """
    gagnant=0
    for i in range(len(joueurs)):
        if joueurs[i][1]>joueurs[gagnant][1]:
            gagnant=i
    return gagnant