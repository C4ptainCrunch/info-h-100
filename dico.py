#!/usr/bin/env python
# -*- coding: utf-8 -*-


def verifier(mot, dico):
    """
        Vérifie qu'un mot est bien dans le dictionnaire
        
        Arguments :
        mot (string) : Mot à vérifier, en majuscules.
        dico (tuple) : Tuple contenant tous les mots autorisés, en majuscules et sans diacritiques
        
        Valeur de retour : (bool)
        Retourne True si le mot est dans le dictionnaire, False sinon
        """
    return mot in dico