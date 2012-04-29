chevalet =  ['S', 'W', 'E', 'G', 'P', 'I', 'S'] 
mot =  PISE 
lettresSup =  []


>>> print verifierChevalet(chevalet, mot, lettresSup)

True

######################################

chevalet =  ['T', 'N', 'I', 'N', 'T', 'V', 'B'] 
mot =  TINS 
lettresSup =  ['S']

>>> print verifierChevalet(chevalet, mot, lettresSup)

True

######################################

chevalet =  ['W', 'G', 'S', 'O', 'J', 'O', 'N'] 
mot =  SINGE 
lettresSup =  ['I']


>>> print verifierChevalet(chevalet, mot, lettresSup)

False