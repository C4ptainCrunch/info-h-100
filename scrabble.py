#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cli
import dico
import humain
import joueur
import ordi
import plateau
import sac


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

def chargerMultiplicateurs(chemin):
    """
        retourne la liste des lettres multiplicatrices : position(x) - position(y) - multiplicateur de mot - multiplicateur de lettre
    """
    fichier = open(chemin)
    liste = []
    for ligne in fichier:
        array = ligne.split(' ')
        array[-1] = array[-1].rstrip()
        liste.append(array)
    return liste

def main():
    #initialisation des variables
    Dico=chargerDico('assets/french.dic')
    multiplicateurs=chargerMultiplicateurs('assets/multiplicateurs')
    Plateau=plateau.init(multiplicateurs)
    lettres=chargerLettres('assets/french.let')
    valeurs=chargerValeurs(lettres)
    Sac=sac.init(lettres)
    joueurs=[]

    nbreJoueurs=cli.demanderJoueur()
    for i in range(nbreJoueurs):
        joueurs.append(joueur.init(Sac))
    manche = 0
    #boucle = manche (tour de plateau)
    while len(Sac)>0:
        manche += 1
        cli.info('Manche numéro '+str(manche))
        #Boucle pour chaque joueur
        for i in range(int(nbreJoueurs)):
            if len(Sac)==0:
                break
            cli.afficher(Plateau)
            cli.info('C\'est au tour du joueur '+str(i+1))
            chevalet = joueurs[i][0]
            cli.afficherChevalet(chevalet)
            points=0
            tourFini=False
            while points==0 and not tourFini:
                mot=cli.demanderMot()   
                if mot == False:
                    delete = cli.demanderJeter()
                    cli.info('Vous jetez la lettre '+delete)
                    chevalet.remove(delete)
                    joueur.remplirChevalet(chevalet, Sac)
                    tourFini = True
                else:
                    posx=int(cli.demande("ligne ? "))
                    posy=int(cli.demande("colonne ? "))
                    dir=int(cli.demande("direction ? "))
                    points=plateau.placer(Plateau, mot, (posx,posy), dir, Dico, joueurs[i][0], valeurs)
                    if points!=0:
                        joueur.ajouterPoints(points, joueurs[i])
                        joueur.remplirChevalet(chevalet, Sac)
                    else:
                        print "Vous vous êtes trompés."
            #Fin du tour
            print "Joueur "+str(i+1)+" : "+str(joueurs[i][1])+" points."
        
    cli.afficher(Plateau)
    print "Il n'y a plus de lettre dans le sac ! Le jeu est fini."
    gagnant=joueur.gagnant(joueurs)
    print "Le gagnant est le joueur "+str(gagnant+1)+" avec "+str(joueurs[gagnant][1])+" points."
        


if __name__ == "__main__":
    main()