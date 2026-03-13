from GenericItem import GenericItem

class ForeignItem(GenericItem):

    def __init__(self,nome, prezzo) -> None:
        super().__init(nome, prezzo*1.2)
        