#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plateau
import sac
import joueur

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

def creerSac(lettres):
    lettres = list(lettres)
    for piece in lettres:
        del piece[2]
        pass
    return lettres

###################################
### initialisation des variables###
###################################

Dico=chargerDico("../assets/french.dic")
Plateau=plateau.init()
lettres=chargerLettres("../assets/french.let")
Sac=sac.init(lettres)


#####

joueur1=joueur.init(Sac)
print joueur1["chevalet"]
mot=raw_input("mot ?")
print len(mot)
print joueur.verifierChevalet(joueur1["chevalet"], mot)