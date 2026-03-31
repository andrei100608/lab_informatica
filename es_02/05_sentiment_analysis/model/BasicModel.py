from model.Model import Model

class BasicModel(Model):

    def __init__(self):
        super().__init__()
    
    def train(self,dati,inizio,fine)->None:
        recensioni_positive = 0
        recensioni_negative = 0
        for i in range(inizio,fine):
            if dati[i][1] == '1':
                recensioni_positive +=1 
            else:
                recensioni_negative += 1
        
        if recensioni_positive > recensioni_negative:
            return True
        else:
            return False

    def test(self,dati,inizio,fine):
        corrette = 0
        if self.train(dati,0,inizio-1)==True:
            for i in range(inizio,fine):
                if dati[i][1] == '1':
                    corrette+=1
        else:
            for i in range(inizio,fine):
                if dati[i][1] == '0':
                    corrette+=1
        return corrette/(fine-inizio)


    def start(self,file)->None:
        dati = Model.data(file)
        lunghezza = len(dati)//2

        return self.test(dati,lunghezza+1,len(dati))