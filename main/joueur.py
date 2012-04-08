#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sac

def init(Sac):
    """
        initialise un joueur (chevalet, points)
    """
    joueur={}
    joueur["chevalet"]=creerChevalet(Sac)
    joueur["points"]=0
    return joueur

def creerChevalet(Sac):
    chevalet=[]
    for i in range(0,7):
        chevalet.append(sac.piocher(Sac))
    return chevalet