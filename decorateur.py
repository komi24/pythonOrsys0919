# -*- coding: utf-8 -*-

#def ensure_uppercase(pos):
#    def deco(f):
#        print("Interieur décorateur", pos)
#        def nouvelle_fonction(*args, **kwargs):
#            print('intérieur nouvelle fonction', args)
#            return f(*args, **kwargs)
#        return nouvelle_fonction
#    return deco

def ensure_uppercase(f):
    print("Interieur décorateur")
    def nouvelle_fonction(*args, **kwargs):
        print('intérieur nouvelle fonction', args)
        assert type(args[0]) == str, \
            'Le premier argument doit être une str'
        new_args = (args[0].upper(),) + args[1:]
        return f(*new_args, **kwargs)
    return nouvelle_fonction

@ensure_uppercase
def dire_bonjour(toto):
    print("Bonjour %s"%(toto))
    

@ensure_uppercase
def dire_bonjour_complexe(nom, age):
    print("Bonjour %s. J'ai %d ans"%(nom, age))
    


dire_bonjour("martin")
dire_bonjour_complexe("léa", 43)
dire_bonjour("Jeanne")
