#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
POUR LES EXEMPLES DES FONCTIONS, VOIR :
"doc/examples/nomdumodule/nomdelafonction.ex"
"""

import string
import unicodedata


def asciiConvert(chaine):
    """Convertit une chaine  encodée en UTF-8 en une autre chaine UTF-8
        lowercase en transformant toutes les lettres accentuées en leur
        équivalent en minuscule non accentué
        (supprimme aussi les caractères non alphanumériques)
        
        Arguments :
        chaine (string) : chaine à convertir
        
        Valeur de retour : (string)
        chaine convertie
    """
    data = chaine.decode('utf-8')
    return ''.join(x for x in unicodedata.normalize('NFKD', data) if \
                   unicodedata.category(x)[0] == 'L').lower()



def afficher(plateau):
    """Affiche le plateau avec des . à la place des cases vides
        des #2 pour les cases mot compte double
        des #3 pour les cases mot compte triple
        des %2 pour les cases lettre compte triple
        des %3 pour les cases lettre compte triple
        Affiche aussi les coordonnées à gauche et en haut du plateau
        
        Arguments :
        plateau (liste) : Le plateau de jeu
        
        Valeur de retour : (None)
    """
    espace = '\t'
    print espace,
    for y in range(0,15):
        print str(y)+espace,
    print '\n\n'
    i = 0
    for x in plateau:
        print str(i)+espace,
        i += 1
        for case in x:
            if case == (1,1): #normale
                print '.'+espace,
            elif case == (2,1): #mot double
                print '#2'+espace,
            elif case == (3,1): #mot triple
                print '#3'+espace,
            elif case == (1,2): #lettre double
                print '%2'+espace,
            elif case == (1,3): #lettre triple
                print '%3'+espace, 
            else:
                print str(case)+espace,
        print '\n\n'


def demande(phrase):
    """Affiche une phrase et un espace après sur STDOUT
        et attend une entrée sur STDIN
        +easteregg !
        
        Arguments :
        phrase (string) : La phrase à afficher
        
        Valeur de retour : (string) Ce que python  à récupéré su STDIN
    """
    retour=raw_input(phrase+' ')
    if retour==42:
        print 'Vous avez trouvé la réponse : Bravo !'
        quit()
    return retour

def info(phrase):
    """Affiche une phrase sur STDOUT
        
        Arguments :
        phrase (string) : La phrase à affiche
        
        Valeur de retour : (None)
    """
    print phrase

def afficherChevalet(chevalet):
    """Affiche le chevalet sur STDOUT
        
        Arguments :
        chevalet (liste) : Liste des lettres du chevalet du joueur
        
        Valeur de retour : (None)
    """
    print 'Chevalet :',
    for lettre in chevalet:
        print lettre + ' ',
    print ''

def demanderJoueur():
    """Appelle demande() tant que l'utilisateur
        n'a pas rentré un nombre entre 1 et 4 compris
        
        Valeur de retour : (int) compris entre 1 et 4
    """
    nb = 0
    while not (0 < nb < 5):
        nb = demande('Nombre de joueurs ?')
        if nb.isdigit():
            nb = int(nb)
    return nb

def demanderJeter():
    """Appelle demande() tant que l'utilisateur
        n'a pas renté une lettre de l'aphabet ou un retour à la ligne
        
        Valeur de retour : (str) lettre de l'alphabet, en maj.
    """
    delete = '%' #Non alpha et non vide pour rentrer dans la boucle min. 1 fois
    while not (delete == '' or(len(delete) == 1 and delete.isalpha())):
        delete = demande('Quelle lettre voulez vous jeter ? Tapez enter pour finir votre tour.')
        if delete.isalpha():
            delete = delete.upper()
    return delete

def demanderMot():
    """Demande à l'utilisateur un mot à former
        
        Valeur de retour :
            Soit (bool) False si l'utilisateur a entré un retour à la linge
            Soit (string) Un mot en majuscules,
            uniquement constitué de lettres ASCII
    """
    mot = asciiConvert(demande('Quel mot voulez-vous former ? '
                               +'Tapez enter pour jeter des lettres.'))
    
    return (False if mot is '' else mot.upper())

def demanderCoord(sens):
    """Appelle demande() tant que l'utilisateur
        n'a pas rentré un nombre entre 0 et 14 compris
        
        Valeur de retour : (int) compris entre 0 et 14
    """
    coord = -1
    while not (0 <= coord <= 14):
        coord = demande('Numéro de '+sens+' ?')
        if coord.isdigit():
            coord = int(coord)
    return coord

def demanderDirection():
    """Appelle demande() tant que l'utilisateur
        n'a pas rentré '0' ou '1'
        
        Valeur de retour : (int) 0 ou 1
    """
    sens = -1
    while not (sens == 1 or sens == 0):
        sens = demande('Dans quel sens voulez-vous placer le mot ? (0 = horizontal, 1 = vertical)')
        if sens.isdigit():
            sens = int(sens)
    return sens

    
