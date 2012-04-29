#!/usr/bin/env python
# -*- coding: utf-8 -*-
import cli
import dico
import joueur
import plateau
import sac


def chargerDico(chemin):
    """
    Charge en mémoire le dictionnaire du Scrabble.
    
    Arguments :
        chemin (string) : chemin du fichier dictionnaire
    
    Valeur de retour : (tuple)
        Ensemble des mots du dictionnaire
    """
    fichier = open(chemin)
    liste = []
    for mot in fichier:
        liste.append(mot.rstrip())
    return tuple(liste)

def chargerLettres(chemin):
    """
    Charge en mémoire la liste des lettres, le nombre qu'il y en a et le nombre
    de points qu'elle vaut pour le jeu de Scrabble.
    
    Arguments :
        chemin (string) : chemin du fichier des lettres
    
    Valeur de retour : (liste)
        Liste des lettres, du nombre qu'il y en a et du nombre de points
        qu'elles vallent pour le jeu de Scrabble.
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
    Retourne un dictionnaire qui associe à chaque lettre le nombre de points
    qu'elle vaut
    
    Arguments :
        lettres (liste) : Liste des lettres, du nombre qu'il y en a et du nombre de points qu'elles vallent pour le jeu de Scrabble.
    
    Valeur de retour : (dictionnaire)
        valeurs : Associe à chaque lettre le nombre de points qu'elle vaut
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
    """
    Initialise un jeu de scrabble et joue toute la partie.
    
    Arguments : /
    Valeur de retour : /
    """
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
            while not tourFini:
                mot=cli.demanderMot()   
                if mot == False: #Si le joueur veut jeter une lettre
                    #Valeur non alphabétique et non vide
                    #pour rentrer dans la boucle min. 1 fois
                    delete = '%' 
                    #Tant que le joueur veut jeter des lettres
                    while delete != '':
                        delete = cli.demanderJeter()
                        if delete in chevalet:
                            cli.info('Vous jetez la lettre '+delete)
                            chevalet.remove(delete)
                            joueur.remplirChevalet(chevalet, Sac)
                        else : 
                            cli.info('Vous n\'avez pas cette lettre,\
veuillez recommencer.')
                    tourFini = True #Quand le joueur ne veut plus jeter
                    #de lettres, on finit le tour
                else: #Si je joueur a rentré un mot
                    posx=int(cli.demanderCoord('ligne'))
                    posy=int(cli.demanderCoord('colonne'))
                    dir=int(cli.demanderDirection())
                    points=plateau.placer(Plateau, mot, (posx,posy),
                                          dir, Dico, joueurs[i][0], valeurs)
                    if points!=0: #Si le mot a été placé
                        joueur.ajouterPoints(points, joueurs[i])
                        joueur.remplirChevalet(chevalet, Sac)
                        tourFini = True
                    else:
                        cli.info('Vous vous êtes trompé, veuillez recommencer.')
            #Fin du tour
            cli.info('Nombre de points gagnés : '+str(points))
            cli.info('Joueur '+str(i+1)+' : '+str(joueurs[i][1])+' points.')
    #Fin du jeu
    cli.afficher(Plateau)
    cli.info('Il n\'y a plus de lettre dans le sac ! Le jeu est fini.')
    gagnant=joueur.gagnant(joueurs)
    cli.info('Le gagnant est le joueur '
             +str(gagnant+1)+' avec '+str(joueurs[gagnant][1])+' points.')
        


if __name__ == "__main__":
    main()