#!/usr/bin/env python
# -*- coding: utf-8 -*-

import plateau
import sac

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

###################################
### initialisation des variables###
###################################

Dico=chargerDico("../assets/french.dic")
Plateau=plateau.init()
lettres=chargerLettres("../assets/french.let")
Sac=sac.init(lettres)

#####

print Sac
print sac.piocher(Sac)
print Sac