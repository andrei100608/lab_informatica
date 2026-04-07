class Book:

    def __init__(self,nome,autore,anno,genere):
        self.nome = nome
        self.autore = autore
        self.anno = anno
        self.genere = genere

    # metodo che mi permette di fare la print dell'oggetto
    def __str__(self):
        return self.nome + " " + self.autore + " " + str(self.anno) + " " + self.genere