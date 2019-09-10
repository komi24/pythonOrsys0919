# -*- coding: utf-8 -*-

#import MonPackage

#MonPackage.dire_bonjour()

#import MonPackage.salutations
#
#MonPackage.salutations.dire_bonjour()
#MonPackage.salutations.say_hi()
#MonPackage.salutations.fala_bomdia()

#from MonPackage import dire_bonjour, say_hi, fala_bomdia
#
#dire_bonjour()
#say_hi()
#fala_bomdia()

#from MonPackage.Voiture import Voiture
#
#une_voiture = Voiture([2,3],'rouge')
#ma_voiture = Voiture([2,3], nombre_de_place=5)
#print(une_voiture.couleur)
#print(ma_voiture.nombre_de_places)
#print(une_voiture.nombre_de_places)
#print(une_voiture.position)
#une_voiture.position = [12,3]
#print(une_voiture.position)

from ExoBank.Personne import Personne
from ExoBank.Compte import Compte

une_personne = Personne('Jung', 'Justine', 32)
autre_personne = Personne('Dupont', 'Charles', 28)

une_personne.dire_bonjour(autre_personne)

un_compte = Compte(10000)
un_compte.depot(100)
un_compte.retrait(100)


