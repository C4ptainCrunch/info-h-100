plateau =  [[(3, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (3, 1), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (3, 1)], [(1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1)], [(1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1)], [(1, 2), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 2)], [(1, 1), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1)], [(3, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), 'N', 'E', 'E', (1, 1), (1, 2), (1, 1), (1, 1), (3, 1)], [(1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 1)], [(1, 2), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 2)], [(1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1)], [(1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1)], [(3, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (3, 1), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (3, 1)]] 
mot =  CLEF 
position =  (5, 8) 
direction =  1 
dictionnaire = ('AA', ... ,'EXTENUAIT', ... ,'ZYTHUMS')
chevalet =  ['U', 'A', 'S', 'C', 'L', 'E', 'F'] 
valeurs =  {'A': '1', 'C': '3', 'B': '3', 'E': '1', 'D': '2', 'G': '2', 'F': '4', 'I': '1', 'H': '4', 'K': '10', 'J': '8', 'M': '2', 'L': '1', 'O': '1', 'N': '1', 'Q': '8', 'P': '3', 'S': '1', 'R': '1', 'U': '1', 'T': '1', 'W': '10', 'V': '4', 'Y': '10', 'X': '10', 'Z': '10'}


>>> print placer(plateau, mot, position, direction, dictionnaire, chevalet, valeurs)

17

######################################

plateau =  [[(3, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (3, 1), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (3, 1)], [(1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1)], [(1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1)], [(1, 2), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 2)], [(1, 1), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), 'C', (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), 'L', (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1)], [(3, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), 'N', 'E', 'E', (1, 1), (1, 2), (1, 1), (1, 1), (3, 1)], [(1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), 'F', (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)], [(1, 1), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 1)], [(1, 2), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 2)], [(1, 1), (1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1), (1, 1)], [(1, 1), (2, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (2, 1), (1, 1)], [(3, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (1, 1), (3, 1), (1, 1), (1, 1), (1, 1), (1, 2), (1, 1), (1, 1), (3, 1)]] 
mot =  NEESIX 
position =  (7, 7) 
direction =  0 
dictionnaire = ('AA', ... ,'EXTENUAIT', ... ,'ZYTHUMS')
chevalet =  ['E', 'E', 'D', 'G', 'S', 'I', 'X'] 
valeurs =  {'A': '1', 'C': '3', 'B': '3', 'E': '1', 'D': '2', 'G': '2', 'F': '4', 'I': '1', 'H': '4', 'K': '10', 'J': '8', 'M': '2', 'L': '1', 'O': '1', 'N': '1', 'Q': '8', 'P': '3', 'S': '1', 'R': '1', 'U': '1', 'T': '1', 'W': '10', 'V': '4', 'Y': '10', 'X': '10', 'Z': '10'}


>>> print placer(plateau, mot, position, direction, dictionnaire, chevalet, valeurs)

False