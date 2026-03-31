from Player import Player
from random import randint

class CpuPlayer(Player):

    def __init__(self,nome="local"):
        super().__init__(nome)
    
    def genera_numero(self,old_guess,stringa,n=0):
        if (stringa=="troppo basso"):
            return old_guess+1
        elif (stringa=="troppo alto"):
            return old_guess-1
        elif n>0:
            return randint(0,n+1)
        return -1