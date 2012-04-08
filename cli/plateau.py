#!/usr/bin/env python
# -*- coding: utf-8 -*-

def afficher(plateau):
    
    for x in plateau:
        for case in x:
            print case+' '
        print '\n'
        