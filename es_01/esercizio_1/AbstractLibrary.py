from abc import ABC,abstractmethod

class AbstractLibrary(ABC):

    def __init__(self):
        pass

    @abstractmethod
    def add_book(self,book):
        pass

    @abstractmethod
    def show_books(self):
        pass
    
    
