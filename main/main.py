#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plateau
import sac
import joueur
import cliPlateau

def chargerDico(chemin):
    fichier = open(chemin)
    liste = []
    for mot in fichier:
        liste.append(mot.rstrip())
    return tuple(liste)

def chargerLettres(chemin):
    """
        retourne la liste des lettres, le nombre qu'il y en a et la valeur en points
    """
    fichier = open(chemin)
    liste = []
    for ligne in fichier:
        array = ligne.split(' ')
        array[-1] = array[-1].rstrip()
        liste.append(array)
    return liste

def chargerValeurs(lettres):
    """
        retourne un dictionnaire avec comme clé la lettre et comme valeur le nombre de points que vaut la lettre
    """
    valeurs={}
    for i in lettres:
        valeurs[i[0]]=i[2]
    return valeurs

####################################
### initialisation des variables ###
####################################

Dico=chargerDico("../assets/french.dic")
Plateau=plateau.init()
lettres=chargerLettres("../assets/french.let")
valeurs=chargerValeurs(lettres)
Sac=sac.init(lettres)

####################################
######## Déroulement du jeu ########
####################################

joueur1=joueur.init(Sac)
while 1!=2:
    cliPlateau.afficher(Plateau)
    print joueur1["chevalet"]
    mot=raw_input("mot ? ")
    pos1=int(raw_input("ligne ? "))
    pos2=int(raw_input("colonne ? "))
    dir=int(raw_input("direction ? "))
    points=plateau.placer(Plateau, mot, (pos1,pos2), dir, Dico, joueur1["chevalet"], valeurs)
    joueur.ajouterPoints(points, joueur1)
    joueur.remplirChevalet(joueur1["chevalet"], Sac)
    print joueur1["points"]