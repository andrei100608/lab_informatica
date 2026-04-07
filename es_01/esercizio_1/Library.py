from Book import *
from AbstractLibrary import *

class Library(AbstractLibrary):
    
    def __init__(self):
        super().__init__()
        self.libri = []
        """
        self.lista_autori = {}
        self.lista_anni = {}
        self.lista_generi = {}
        """

    def add_book(self,book):
        self.libri.append(book)
        """
        self.autore[book.nome] = book.autore
        self.anno[book.nome] = book.anno
        self.genere[book.nome] = book.genere
        """

    def show_books(self):
        for libro in self.libri:
            print(libro)
            #print(libro + " " + self.autore[libro] + " " + str(self.anno[libro]) + " " + self.genere[libro])

    def find_books_by_author(self,autore):
        ris = []
        for libro in self.libri:
            if libro.autore == autore:
                ris.append(libro)
        return ris
    
    def find_books_by_year(self,anno):
        ris = []
        for libro in self.libri:
            if libro.anno == anno:
                ris.append(libro)
        return ris