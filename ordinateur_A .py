import socket

# ============================================
# ORDINATEUR B (SERVEUR)
# ============================================
def create_server():
    # Étape 1: Créer un socket TCP/IP
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Étape 2: Définir l'adresse et le port
    host = 'localhost'  # Remplacez par l'IP de l'ordinateur B
    port = 12345
    
    # Étape 3: Lier le socket à l'adresse et au port
    server_socket.bind((host, port))
    
    # Étape 4: Mettre le socket en mode écoute
    server_socket.listen(1)
    print(f"Serveur en écoute sur {host}:{port}")
    
    try:
        while True:
            # Étape 5: Accepter une connexion
            client_socket, client_address = server_socket.accept()
            print(f"Connexion établie avec {client_address}")
            
            # Étape 6: Recevoir le message
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Message reçu: {message}")
            
            # Étape 7: Vérifier si le message est "bonjour"
            if message.lower() == "bonjour":
                # Étape 8: Envoyer la réponse
                response = "salut bonjour"
                client_socket.send(response.encode('utf-8'))
                print(f"Réponse envoyée: {response}")
            
            # Étape 9: Fermer la connexion client
            client_socket.close()
            
    except KeyboardInterrupt:
        print("\nArrêt du serveur...")
    finally:
        # Étape 10: Fermer le socket serveur
        server_socket.close()
