# -*- coding: utf-8 -*-

for i in range(100):
    print(i)
    
for i in [4,9,63,8,7]:
    print(i)
    
# For sur dictionnaire affiche les clés
for i in {'nom': 'Bolnet', 'prenom': 'Mickael'}:
    print(i)

# Affiche les valeurs
for i in ({'nom': 'Bolnet', 'prenom': 'Mickael'}).values():
    print(i)

# Affiche les (clé, valeur)
for i in ({'nom': 'Bolnet', 'prenom': 'Mickael'}).items():
    print(i)


for i, val in enumerate([4,9,63,8,7]):
    print(i, val)

liste_1 = [1,4,3,6,5,12,43]
liste_2 = [0,4,8,12,6]

for i,j in zip(liste_1, liste_2):
    print(i,j)


print("--------------ITERTOOLS----------------")
from itertools import product

for i,j in product(range(4), range(3)):
    print(i,j)

for i,j in product([4,3,2], [12,8,17]):
    print(i,j)

