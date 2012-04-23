#!/usr/bin/env python
# -*- coding: utf-8 -*-

import main.plateau
import main.sac
import main.joueur
import cli

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

def main():
    ####################################
    ### initialisation des variables ###
    ####################################

    Dico=chargerDico("assets/french.dic")
    Plateau=plateau.init()
    lettres=chargerLettres("assets/french.let")
    valeurs=chargerValeurs(lettres)
    Sac=sac.init(lettres)
    joueurs=[]

    ####################################
    ######## Déroulement du jeu ########
    ####################################

    nbreJoueurs=raw_input("Nombre Joueurs ? ")
    for i in range(int(nbreJoueurs)):
        joueurs.append(joueur.init(Sac))

    while True: #Boucle pour chaque tour
        print "NOUVEAU TOUR"
        for i in range(int(nbreJoueurs)): #boucle pour chaque joueur
            cli.plateau.afficher(Plateau)
            print "JOUEUR "+str(i+1)
            print joueurs[i][0]
            points=0
            fini=False
            while points==0 and fini==False:
                mot=cli.utilisateur.demande("mot ? ")
                pos1=int(cli.utilisateur.demande("ligne ? "))
                pos2=int(cli.utilisateur.demande("colonne ? "))
                dir=int(cli.utilisateur.demande("direction ? "))
                points=plateau.placer(Plateau, mot, (pos1,pos2), dir, Dico, joueurs[i][0], valeurs)
                if not points==0:
                    joueur.ajouterPoints(points, joueurs[i])
                    joueur.remplirChevalet(joueurs[i][0], Sac)
                elif mot=="0":
                    print "Vous passez votre tour"
                    fini=True
                else:
                    print "Vous vous êtes trompés."
            print "Joueur "+str(i+1)+" : "+str(joueurs[i][1])+" points."