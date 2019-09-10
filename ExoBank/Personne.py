# -*- coding: utf-8 -*-

class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age

    def dire_bonjour(self, autre_personne):
        assert type(autre_personne) == Personne, \
            "Erreur : autre personne doit être de classe Personne"
        print("Bonjour %s. Je m'appelle %s %s"%(
                autre_personne.prenom,
                self.prenom,
                self.nom))
    