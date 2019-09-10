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
        