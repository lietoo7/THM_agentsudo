import sys
import socket

def enumerate_ports(host):
    # Parcourez les ports de 1 à 65535 et vérifiez s'ils sont ouverts
    open_ports = []
    for port in range(1, 65536):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Réglez un délai d'attente court pour la connexion
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return open_ports

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Utilisation: python script.py <adresse_ip>")
        sys.exit(1)

    host = sys.argv[1]
    open_ports = enumerate_ports(host)

    if open_ports:
        print(f"Ports ouverts sur l'adresse IP {host}:")
        for port in open_ports:
            print(f"Port {port} est ouvert")
    else:
        print(f"Aucun port ouvert trouvé sur l'adresse IP {host}.")

