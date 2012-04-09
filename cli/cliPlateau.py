#!/usr/bin/env python
# -*- coding: utf-8 -*-

def cliPlateauafficher(plateau):
    espace = '\t'
    print espace,
    for y in range(0,15):
        print str(y)+espace,
    print ''
    i = 0
    for x in plateau:
        print str(i)+espace,
        i += i
        for case in x:
            if case == None:
                print '+'+espace,
            else:
                print str(case)+espace,
        print '\n\n'
        




