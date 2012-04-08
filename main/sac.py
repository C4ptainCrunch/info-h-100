#!/usr/bin/env python
# -*- coding: utf-8 -*-

def init(lettres):
    sac=[]
    for lettre in lettres:
        n=int(lettre[1])
        for i in range(n):
            sac.append(lettre[0])
    return sac