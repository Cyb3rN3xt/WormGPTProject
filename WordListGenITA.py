import random
import string
from datetime import datetime, timedelta

# Funzione per generare una password
def generate_passwords(tutte_parole, date_generator):
    caratteri_speciali = "!@#$%^&*()"
    max_length = 20
    
    while True:
        parola = random.choice(tutte_parole)
        
        # Aggiungi numeri casuali, date di nascita o età
        if random.choice([True, False]):
            if random.choice([True, False]):
                parola += str(random.randint(0, 99))  # Età casuale
            else:
                parola += next(date_generator)  # Data di nascita
        
        # Aggiungi caratteri speciali casuali
        if random.choice([True, False]):
            parola += ''.join(random.choice(caratteri_speciali) for _ in range(random.randint(1, 3)))
        
        # Assicurati che la password sia entro una lunghezza ragionevole
        if len(parola) < max_length:
            yield parola

# Funzione per generare date di nascita a partire dal 1950
def generate_dates():
    start_date = datetime(1950, 1, 1)
    while True:
        yield start_date.strftime("%d%m%Y")
        start_date += timedelta(days=random.randint(1, 365))  # Aggiungi giorni casuali

# Funzione per scrivere le password in un file fino a raggiungere la dimensione desiderata
def write_passwords_to_file(file_path, target_size_gb, tutte_parole):
    target_size = target_size_gb * 1024 * 1024 * 1024  # Converti GB in byte
    current_size = 0
    date_generator = generate_dates()
    
    with open(file_path, "w") as file:
        for password in generate_passwords(tutte_parole, date_generator):
            file.write(password + "\n")
            current_size += len(password) + 1  # +1 per il carattere di nuova riga
            if current_size >= target_size:
                break

# Funzione principale per raccogliere input e generare la wordlist
def main():
    # Raccogli input dall'utente
    nome = input("Nome: ")
    eta = input("Età: ")
    citta = input("Città: ")
    paese = input("Paese: ")
    nome_cane = input("Nome di cane: ")
    nome_gatto = input("Nome di gatto: ")
    squadra_calcio = input("Squadra di calcio: ")
    data_di_nascita = input("Data di nascita (formato ddmmyyyy): ")
    
    # Lista di parole comuni e non comuni italiane
    parole_comuni = [
        "amore", "casa", "scuola", "lavoro", "tempo", "giorno", "notte", "anno", "vita", "uomo",
        "donna", "bambino", "ragazzo", "ragazza", "padre", "madre", "fratello", "sorella", "amico", "amica"
    ]
    
    parole_non_comuni = [
        "anticonstituzionale", "esofagodermatodigiunoplastica", "calunniatrice", "contaminazione", "idiosincrasia",
        "poliedrico", "telecinesi", "eterocromia", "filantropico", "paradisiaco"
    ]
    
    # Combina tutte le parole
    tutte_parole = (parole_comuni + parole_non_comuni + [nome] + [eta] + [citta] + [paese] + [nome_cane] + [nome_gatto] +
                    [squadra_calcio] + [data_di_nascita])

    # Scrivi le password nel file
    write_passwords_to_file("wordlist.txt", 50, tutte_parole)

# Esegui la funzione principale
if __name__ == "__main__":
    main()
