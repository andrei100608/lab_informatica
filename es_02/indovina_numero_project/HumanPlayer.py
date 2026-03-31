from Player import Player

class HumanPlayer(Player):

    def __init__(self,nome):
        super().__init__()
        self.nome = nome
    
    def genera_numero(self):
        while (True):
            try:
                num = int(input("digita numero: "))
                break
            except:
                print("inserisci numero valido")
        return num