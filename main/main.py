#!/usr/bin/env python
# -*- coding: utf-8 -*-
import plateau
def chargerDico(chemin):
    fichier = open(chemin)
    liste = []
    for mot in fichier:
        liste.append(mot.rstrip())
    return tuple(liste)

def chargerLettres(chemin):
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

#plat=plateau.init()
#print plateau.placer(plat, "mdfsfsfqsdddddot", (0,0), 1)
#afficher(plat)