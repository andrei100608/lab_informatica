from model.Model import Model
import csv

class WordModel(Model):

    def __init__(self):
        super().__init__()
        self.positive = dict()
        self.negative = dict()
        
    
    def train(self,dati,inizio,fine)->None:
        for i in range(inizio,fine):
            parole = dati[i][0].strip('"').split() #dati-> lista di tuple, dati[i] -> tupla, dati[i][0]->testo
            if dati[i][1] == '0':
                for parola in parole:
                    if parola not in self.negative:
                        self.negative[parola] = 1
                    else:
                        self.negative[parola] += 1
            elif dati[i][1] == '1':
                for parola in parole:
                    if parola not in self.positive:
                        self.positive[parola] = 1
                    else:
                        self.positive[parola] += 1
        return
                


    def test(self,dati,inizio,fine)->float:
        predicted_label = []
        corrette = 0
        for i in range(inizio,fine):
            parole = dati[i][0].strip('"').split()
            valutazione = 0
            for parola in parole:
                if parola in self.positive and parola in self.negative:
                    score = self.positive[parola]-self.negative[parola]
                    totali = self.positive[parola]-self.negative[parola]
                    if (score/totali>0.1):
                        if score > 0:
                            valutazione+=1
                        elif score < 0:
                            valutazione-=1
                elif parola in self.positive:
                    valutazione+=1
                elif parola in self.negative:
                    valutazione-=1

            if (valutazione>=0):
                predicted_label.append((i,1))
                if dati[i][1]=='1':
                    corrette+=1
            else:
                predicted_label.append((i,0))
                if dati[i][1]=='0':
                    corrette+=1
        
        self.crea_file('/home/biar/Desktop/lab_informatica/05_sentiment_analysis/text.tsv',dati,predicted_label,inizio,fine)
        accuracy = corrette/(fine-inizio)
        return accuracy

    
    def crea_file(self,file1,dati,predicted_label,inizio,fine):
        with open(file1,'w',encoding='utf-8') as f:
            writer = csv.writer(f, delimiter="\t")  # separatore TAB
            writer.writerow(["review", "label","predicted_label"])    # header

            for i in range(0,fine):
                if i < inizio:
                    writer.writerow([dati[i][0],dati[i][1],""])
                elif i>=inizio:
                    writer.writerow([dati[i][0],dati[i][1],predicted_label[i-inizio][1]])

    def start(self,file):
        dati = Model.data(file)
        lunghezza = len(dati)//2

        self.train(dati,0,lunghezza)
        return self.test(dati,lunghezza+1,len(dati))
