#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sac

def init(Sac):
    """Initialise un joueur
        
        Arguments :
        Sac (list) : Liste de lettres.
        
        Valeur de retour : (list)
        Liste de 2 éléments : le premier étant un chevalet (list) et le deuxième 0 (int) étant le nombre de points du joueur
    """
    joueur=[]
    joueur.append(creerChevalet(Sac))
    joueur.append(0)
    return joueur

def creerChevalet(Sac):
    """Crée un chevalet en enlevant des lettres de Sac
        
        Arguments :
        Sac (list) : Liste des lettres du sac.
        
        Valeur de retour : (list)
        Liste de 7 éléments : chaque élément étant une lettre majuscule (string)
    """
    chevalet=[]
    for i in range(0,7):
        chevalet.append(sac.piocher(Sac))
    return chevalet

def ajouterPoints(n, joueur):
    """Ajoute n points à un joueur
        
        Arguments :
        n (int) : Liste de lettres.
        
        Valeur de retour : (list)
        Liste de 7 éléments : chaque élément étant une lettre majuscule (string)
    """
    joueur[1]+=n

def remplirChevalet(chevalet, Sac):
    """Re-remplit le chevalet pour qu'il contienne 7 lettres
        
        Arguments:
        chevalet (list) : chevalet à re-remplir
        Sac (list) : Liste des lettres du sac
        
        Valeur de retour : (None)
    """
    for i in range(len(chevalet), 7):
        chevalet.append(sac.piocher(Sac))

def retirerChevalet(chevalet, mot, lettresExistantes):
    """Retire le mot du chevalet
        (sans retirer les lettres du mot qui sont déjà sur le plateau)
        Attention, d'abord vérifier que mot dans chevalet.
        
        Arguments:
        chevalet (list) : chevalet à re-remplir
        mot (string) : mot que l'utilisateur a entré
        lettresExistantes (string) : lettres de mot qui sont déjà sur le plateau 
        
        Valeur de retour : (None)
    """
    chevalet.extend(lettresExistantes)
    for lettre in mot:
        chevalet.remove(lettre)

def verifierChevalet(chevalet, mot, lettresSup):
    """Vérifie qu'un mot que le joueur va poser est bien dans le chevalet,
        (en comptant que certaines lettres sont déjà sur le plateau)

        Arguments:
        mot (string) : mot que l'utilisateur a entré
        lettresExistantes (string) : lettres de mot qui sont déjà sur le plateau 
        
        Valeur de retour : (bool)
            True si le mot est dans le chevalet,
            False sinon
    """
    test=[] # Si lettresSup=False, on veut retourner False
    #et donc rentrer dans la condition de la liste vide
    #(dans la condition ci-dessous)
    if not lettresSup==False:
        test+=lettresSup+chevalet
    for lettre in mot:
        if not test.count(lettre)==0:
            test.remove(lettre)
        else:
            return False
    return True

def gagnant(joueurs):
    """Depuis la liste des joueurs,
        retourne l'indice du joueur qui le plus de points
        
        Arguments:
        joueurs (list) : La liste des joueurs
       
        Valeur de retour : (int)
        L'indice du joueur ayant le plus de points
    """
    gagnant=0
    for i in range(len(joueurs)):
        if joueurs[i][1]>joueurs[gagnant][1]:
            gagnant=i
    return gagnant