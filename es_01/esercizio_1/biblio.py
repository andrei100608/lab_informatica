from Library import *
from FastLibrary import *
from Book import *
from random import randint

"""
book1 = Book("1984","George Orwell",1949,"Distopia")
book2 = Book("Il nome della rosa","Umberto Eco",1980,"Storico")
"""

#library = Library()
fastLibrary = FastLibrary()

# genero 100000 libri e li aggiungo
for i in range(1,100001):
    titolo = f"libro_{i}"
    random = randint(0,100)
    fastLibrary.add_book(Book(titolo,f"autore_{random}",2000+i%25,"Fantascienza"))

"""
fastLibrary.add_book(book1)
fastLibrary.add_book(book2)
"""

fastLibrary.show_books()

print("Libri di autore_1:")
for book in fastLibrary.find_books_by_author("autore_1"):
    print(book)

print("Libri pubblicati nel 2015:")
for book in fastLibrary.find_books_by_year(2015):
    print(book)

