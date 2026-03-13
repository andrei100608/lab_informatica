from e_store.store_item.GenericItem import GenericItem 
from e_store.store.Store import Store

def main():
    # Crea alcuni prodotti
    item1 = GenericItem("Laptop", 1200)
    item2 = GenericItem("Smartphone", 800)

    # Crea un negozio
    store = Store(500000)

    # Crea alcuni clienti e aggiungili al negozio
    store.crea_utente("M", 15000, "p","")
    store.crea_utente("Giulia", 25000, "giulia123","")
    store.crea_utente("Francesco", 10000, "francesco123", "promotional")

    # Aggiungi i prodotti all'inventario
    store.compra_oggetti(item1, 5)
    store.compra_oggetti(item2, 10)

    # Login - Chiediamo il nome utente e la password
    customer = None
    while customer is None:
        print("\n--- Login ---")
        username_input = input("Inserisci il tuo nome utente: ")
        password_input = input("Inserisci la tua password: ")

        # Verifica il login del cliente
        customer = store.autentica_utente(username_input, password_input)

    if customer is None:
        print("Nome utente o password errati. Riprova.")

    # Menu interattivo
    while True:
        print(f"\nBenvenuto nel negozio, {customer.nome}!")
        print(f"Saldo disponibile: {customer.denaro}€")
        print("1. Mostra inventario")
        print("2. Acquista prodotto")
        print("3. Esci")

        choice = input("Scegli un'opzione: ")

        if choice == "1":
            store.show_inventory()
        elif choice == "2":
            store.show_inventory()
            product_nome = input("Inserisci il nome del prodotto da acquistare: ")
            quantity = int(input(f"Quanti {product_nome} vuoi comprare? "))

            if store.vende_oggetti_by_nome(product_nome, quantity, customer)!=0:
                print("fatto")
            else:
                print("Prodotto o soldi non disponibile.")
        elif choice == "3":
            print("Arrivederci!")
            break
        else:
            print("Opzione non valida.")


if __name__ == "__main__":
    main()

