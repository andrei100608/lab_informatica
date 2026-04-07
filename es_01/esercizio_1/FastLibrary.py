from Library import *
from AbstractLibrary import *

class FastLibrary(AbstractLibrary):
    
    def __init__(self):
        super().__init__()
        self.libri = {}
        self.lista_autori = {}
        self.lista_anni = {}
        #self.genere = {}

    def add_book(self,book):
        if (book.nome not in self.libri):
            self.libri[book.nome] = book

        # aggiungo libro ad insieme corrispondente a quell'autore
        if (book.autore not in self.lista_autori):
            self.lista_autori[book.autore] = {book}
        else:
            self.lista_autori[book.autore].add(book)

        # aggiungo libro ad insieme corrispondente a quell'anno
        if (book.anno not in self.lista_anni):
            self.lista_anni[book.anno] = {book}
        else:
            self.lista_anni[book.anno].add(book)

        # aggiungo libro ad insieme corrispondente a quel genere
        #if (book.genere not in self.genere):
        #    self.genere[book.genere] = {book}
        #else:
        #    self.genere[book.genere].add(book)

    def show_books(self):
        for libro in self.libri:
            print(self.libri[libro])

    def find_books_by_author(self,autore):
        if (autore in self.lista_autori.keys()):
            return self.lista_autori[autore]
        else:
            return set()
    
    def find_books_by_year(self,anno):
        if (anno in self.lista_anni.keys()):
            return self.lista_anni[anno]
        else:
            return set()