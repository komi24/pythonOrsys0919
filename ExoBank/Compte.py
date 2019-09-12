# -*- coding: utf-8 -*-
class SoldeInsufisantException(Exception):
    pass


class Compte:
    def __init__(self, solde):
        self.solde = solde

    def retrait(self, montant):
        assert montant > 0, \
            "On ne peut pas retirer un montant négatif"
        if montant > self.solde:
            raise SoldeInsufisantException()
            
        self.solde -= montant

    def depot(self, montant):
        assert montant > 0, \
            "On ne peut pas déposer un montant négatif"
        self.solde += montant
    
    def __lt__(self, autre_compte):
        return self.solde < autre_compte.solde

    def __eq__(self, autre_compte):
        return self.solde == autre_compte.solde
    

class CompteEpargne(Compte):
    def __init__(self, solde, interet=10):
        Compte.__init__(self, solde)
        self.interet = interet
        self.anciennete = 0

    def retrait(self, montant):
        assert self.anciennete > 8, "Vous devez attendre encore"
        Compte.retrait(self, montant)


class Test:
    def __init__(self, solde):
        self.solde = 0

class CompteCourant(Compte, Test):
    def retrait(self, montant):
        assert montant > 0, \
            "On ne peut pas retirer un montant négatif"
        if montant > self.solde + 300:
            raise SoldeInsufisantException()
            
        self.solde -= montant





