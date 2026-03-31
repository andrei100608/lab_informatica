from abc import ABC,abstractmethod
import csv

class Model(ABC):

    def __init__(self):
        super().__init__()
    
    def data(file)->list:
        righe = list()

        with open(file,'r',encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            next(csv_reader)
            for riga in csv_reader:
                righe.append((riga[0].strip('"'),riga[1]))
        return righe
    
    @abstractmethod
    def train(self,dati,inizio,fine)->None:
        pass

    @abstractmethod
    def start(self,dati,inizio,fine)->float:
        pass