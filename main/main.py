#!/usr/bin/env python
# -*- coding: utf-8 -*-

def chargerDico(chemin):
    fichier = open(chemin)
    liste = []
    for mot in fichier:
        liste.append(mot.rstrip())
    return tuple(liste)

print chargerDico('assets/french.dic')