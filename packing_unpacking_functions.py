# -*- coding: utf-8 -*-

# Arguments simple
def ma_fonction(arg1, arg2):
    print(arg1)
    print(arg2)

tableau = [2,7]
ma_fonction(*tableau)



# Arguments nommés
def ma_fonction(arg1="", arg2=""):
    print(arg1)
    print(arg2)

tableau = {"arg1":2, "arg2":7}
ma_fonction(**tableau)



# Arguments mixtes
def ma_fonction(arg1, arg2, arg3="", arg4=""):
    print(arg1)
    print(arg2)
    print(arg3)
    print(arg4)

array = [2,7]
dico= {"arg3":2, "arg4":7}
ma_fonction(*array,**dico)

# Récupération Arguments mixtes
def ma_fonction(*args, **kwargs):
    print(args[0])
    print(args[1])
    print(kwargs["arg1"])
    print(kwargs["arg2"])

ma_fonction(2,4,arg1="4", arg2=8)

