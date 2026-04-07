from FastLibrary import *

class RemovableLibrary(FastLibrary):

    def __init__(self):
        super().__init__()

    def remove_book(self,titolo):
        if (titolo in self.libri):
            libro = self.libri[titolo]
            year = self.libri[titolo].anno
            author = self.libri[titolo].autore

            self.lista_anni[year].discard(libro)
            self.lista_autori[author].discard(libro)
            self.libri.pop(titolo)
            return libro