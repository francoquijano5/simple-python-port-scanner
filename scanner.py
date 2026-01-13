import socket # Librería para conexiones de red

def scan_ports(ip, port_list):
    print(f"Iniciando escaneo en: {ip}")
    print("-" * 30)
    
    for port in port_list:
        # Creamos un socket (AF_INET es para IPv4, SOCK_STREAM es para TCP)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1) # Tiempo de espera de 1 segundo
        
        # Intentamos conectar con el puerto
        result = s.connect_ex((ip, port))
        
        if result == 0:
            print(f"[+] Puerto {port}: ABIERTO")
        else:
            # Puedes quitar este 'else' si solo quieres ver los abiertos
            print(f"[-] Puerto {port}: Cerrado")
            
        s.close()

if _name_ == "_main_":
    target_ip = "127.0.0.1" # Escanea tu propia máquina (Localhost)
    ports_to_scan = [21, 22, 80, 443, 3306] # Puertos comunes
    
    scan_ports(target_ip, ports_to_scan)
