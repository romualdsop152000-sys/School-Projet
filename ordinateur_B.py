import socket
# ============================================
# ORDINATEUR A (CLIENT)
# ============================================
def create_client():
    # Étape 1: Créer un socket TCP/IP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Étape 2: Définir l'adresse et le port du serveur
    server_host = 'localhost'  # Remplacez par l'IP de l'ordinateur B
    server_port = 12345
    
    try:
        # Étape 3: Se connecter au serveur
        client_socket.connect((server_host, server_port))
        print(f"Connecté au serveur {server_host}:{server_port}")
        
        # Étape 4: Envoyer le message "bonjour"
        message = "bonjour"
        client_socket.send(message.encode('utf-8'))
        print(f"Message envoyé: {message}")
        
        # Étape 5: Recevoir la réponse
        response = client_socket.recv(1024).decode('utf-8')
        print(f"Réponse reçue: {response}")
        
    except ConnectionRefusedError:
        print("Erreur: Impossible de se connecter au serveur")
    except Exception as e:
        print(f"Erreur: {e}")
    finally:
        # Étape 6: Fermer la connexion
        client_socket.close()

# ============================================
# EXÉCUTION PRINCIPALE
# ============================================
#if __name__ == "__main__":
    # Note: Dans un vrai scénario, exécutez ces fonctions sur des machines séparées
    # Ordinateur B exécute: create_server()
    # Ordinateur A exécute: create_client()
    
    #create_server()    # À exécuter sur l'ordinateur B
   # create_client()    # À exécuter sur l'ordinateur A