# main.py
from model.BasicModel import BasicModel
from model.WordModel import WordModel

if __name__ == "__main__":
    tipo_modello = input("Scegli un modello: word or basic: ").strip().lower()

    if tipo_modello == "word":
        modello = WordModel()
    elif tipo_modello == "basic":
        modello = BasicModel()

    accuracy = modello.start('/home/biar/Desktop/lab_informatica/05_sentiment_analysis/IMDB_validation.csv')
    print("L'accuracy del modello è " + str(accuracy))

    
