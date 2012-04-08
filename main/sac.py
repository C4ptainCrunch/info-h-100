#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def init(lettres):
    sac=[]
    for lettre in lettres:
        n=int(lettre[1])
        for i in range(n):
            sac.append(lettre[0])
    return sac

def piocher(sac):
    i=random.randint(0,len(sac)-1)
    return sac.pop(i)