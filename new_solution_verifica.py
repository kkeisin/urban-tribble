#Esercizio lista prodotti, by Bondar Oleksandr

def riempi():
    Articoli = []
    N = 0
    while N < 3 or N > 99:
        N = int(input("Inserisci quanti articoli vuoi avere (3 - 99): "))
    for i in range(N):
        descrizione = input("Inserisci la descrizione del articolo: ")
        quantita = int(input("Inserisci la quantita del articolo: "))
        data_scad = int(input("Inserisci la data di scadenza del articolo: "))
        Articoli.extend([descrizione, quantita, data_scad])
    
    return Articoli

def cerca(Articoli):
    data_cerc = int(input("Di che data vuoi cercare la scadenza: "))
    prod_scad = [Articoli[i-2] for i in range(2, len(Articoli), 3) if Articoli[i] < data_cerc]
    if prod_scad:
        print("Prodotti scaduti: ")
        for Articoli in prod_scad:
            print(Articoli)
    else:
        print("Non ci sono prodotti scaduti")


def compra(Articoli, Ordini):
    descrizione = input("Inserisci la descrizione del prodotto da aquistare: ")
    quantita_aquist = int(input("Inserisci la quantita dei prodotto da aquistare: "))

    while True:
        try:
            index = Articoli.index(descrizione)
            quantita_prima = Articoli[index + 1]
            if quantita_aquist <= quantita_prima:
                Articoli[index + 1] -= quantita_aquist
                if Articoli[index + 1] <= 5:
                    Ordini.append(descrizione)
                break
            else:
                print("Errore! Inserisci una quantita inferiore.")
                quantita_aquist = input("Inserisci una nuova quantita: ")
        except ValueError:
            print("Descrizione non trovato!")

def riordina(Articoli, Ordini):
    if Ordini:
        ultima_descrizione = Ordini[-1]
        try:
            index = Articoli.index(ultima_descrizione)
            quantita_riordino = int(input("Inserisci quanti nuovi pezzi riordinare: "))
            Articoli[index + 1] += quantita_riordino
        except ValueError:
            print("Descrizione non trovata nella lista.")
    else:
        print("Nessun articolo presente nella lista.")

def stampa(Articoli, Ordini):
    if Articoli:
        print("Lista del magazzino:")
        for i in range(0, len(Articoli), 3):
            print(f"Descrizione: {Articoli[i]}, Quantita: {Articoli[i+1]}, Anno di scadenza: {Articoli[i+2]}")
    else:
        print("Nessun articolo presente")

    if Ordini:
        print("Lista degli ordini:")
        for ordine in Ordini:
            print(ordine)
    else:
        print("Nessun ordine presente")

def main():

    Articoli = []
    Ordini = []
    while True:
        print('''
                \nMenu:
                1. Riempi
                2. Cerca
                3. Compra
                4. Riordina
                5. Stampa
                6. Exit
                ''')
        scelta = input("Scegli una opzione: ")

        if scelta == '1':
            Articoli = riempi()
        elif scelta == '2':
            cerca(Articoli)
        elif scelta == '3':
            compra(Articoli, Ordini)
        elif scelta == '4':
            riordina(Articoli, Ordini)
        elif scelta == '5':
            stampa(Articoli, Ordini)
        elif scelta == '6':
            print("Programma terminato.")
            break
        else:
            print("Scelta non valida. Riprova.")

main()