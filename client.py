import socket

# Crea un socket TCP IPv4.
# Il socket verrà chiuso automaticamente al termine del blocco with.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:

    # Richiede una connessione al server all'indirizzo e porta indicati.
    client.connect(("127.0.0.1", 5000))

    # Legge un messaggio da tastiera.
    # encode() converte la stringa in byte per poterla inviare.
    messaggio = input("Inserisci un messaggio: ")
    client.sendall(messaggio.encode())

    # Riceve fino a 1024 byte dal server.
    # decode() riconverte i byte in una stringa leggibile.
    risposta = client.recv(1024)
    print("Risposta del server:", risposta.decode())