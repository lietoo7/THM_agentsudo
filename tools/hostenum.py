import sys
import socket
import argparse

# Dictionnaire des ports couramment utilisés
common_ports = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    443: "HTTPS",
    3306: "MySQL"
}

def enumerate_ports(host, ports):
    open_ports = []
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def get_service_name(port, protocol='tcp'):
    try:
        service_name = socket.getservbyport(port, protocol)
        return service_name
    except OSError:
        return "Service inconnu"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scanner de ports")
    parser.add_argument("adresse_ip", help="Adresse IP à scanner")
    parser.add_argument("-p", "--ports", help="Liste de ports à scanner (séparés par des virgules)",
                        type=lambda s: [int(port) for port in s.split(',')],
                        default=list(range(1, 65536)))
    parser.add_argument("-U", "--common-ports", help="Scanner uniquement les ports couramment utilisés",
                        action="store_true")

    args = parser.parse_args()
    host = args.adresse_ip

    if args.common_ports:
        ports_to_scan = list(common_ports.keys())
    else:
        ports_to_scan = args.ports

    open_ports = enumerate_ports(host, ports_to_scan)

    if open_ports:
        print(f"Ports ouverts sur l'adresse IP {host}:")
        for port in open_ports:
            service_name = get_service_name(port)
            print(f"Port {port} est ouvert (Service : {service_name})")
    else:
        print(f"Aucun port ouvert trouvé sur l'adresse IP {host}.")
