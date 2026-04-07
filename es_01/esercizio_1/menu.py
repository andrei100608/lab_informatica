from Library import *
from FastLibrary import *
from RemovableLibrary import *
import time

while(True):
    tipo_libreria = input("Scegli il tipo di libreria da usare\nS:slow\nF:fast\nR:removable:\n")

    if (tipo_libreria == "S"):
        library = Library()
        break
    elif(tipo_libreria == "F"):
        library = FastLibrary()
        break
    elif(tipo_libreria == "R"):
        library = RemovableLibrary()
        break

while(True):
    time.sleep(2)
    if isinstance(library,RemovableLibrary):
        comando = input("Scegli la funzione da eseguire\nA:Aggiungi Libro\nR:Rimuovi Libro\nMT: Mostra tutti i libri\nMA: Mostra libri per autore\nMY: Mostra libri per anno\nE: Exit\n")
    else:
        comando = input("Scegli la funzione da eseguire\nA:Aggiungi Libro\nMT: Mostra tutti i libri\nMA: Mostra libri per autore\nMY: Mostra libri per anno\nE: Exit\n")
        if (comando=="R"):
            comando = "comando sbagliato"
    if (comando=="A"):
        titolo = input("Inserisci il titolo del libro da aggiungere: ")
        autore = input("Inserisci il nome dell'autore: ")
        while (True):
            try:
                anno = int(input("Inserisci l'anno del libro: "))
                break
            except ValueError:
                print("valore inserito errato")
                
        genere = input("Inserisci il genere del libro: ")
        libro = Book(titolo,autore,anno,genere)
        library.add_book(libro)
        print("libro inserito: ",libro)
    elif (comando == "R"):
        titolo = input("Inserisci il titolo del libro da rimuovere: ")
        libro = library.remove_book(titolo)
        if (libro):
            print("libro rimosso: ",libro)
        else:
            print("libro non esistente")
    elif (comando == "MT"):
        library.show_books()
    elif (comando == "MA"):
        autore = input("Inserisci il nome dell'autore di cui mostrare i libri: ")
        for libro in library.find_books_by_author(autore):
            print(libro)
    elif (comando == "MY"):
        while(True):
            try:
                anno = int(input("Inserisci l'anno di cui mostrare i libri: "))
                for libro in library.find_books_by_year(anno):
                    print(libro)
                break
            except ValueError:
                print("valore inserito errato")
    elif(comando == "E"):
        print("Libreria chiusa")
        break
    else:
        print("Comando sbagliato")
    