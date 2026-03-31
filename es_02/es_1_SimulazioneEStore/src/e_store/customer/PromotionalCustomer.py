from e_store.customer.GenericCustomer import GenericCustomer
class PromotionalCustomer(GenericCustomer):

    def __init__(self, nome, denaro, password) -> None:
        super().__init__(nome, denaro, password)
        