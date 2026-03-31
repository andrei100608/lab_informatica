from Player import Player
from random import randint

class FastPlayer(Player):

    def __init__(self,nome="local"):
        super().__init__(nome)
    
    def genera_numero(self,old_guess,stringa,max,min=0):
        if (stringa=="troppo basso"):
            return (max+old_guess)//2
        elif (stringa=="troppo alto"):
            return (min+old_guess)//2
        else:
            return max//2