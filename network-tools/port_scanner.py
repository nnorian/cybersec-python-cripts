#port scanner for cybersec learning
#features: multi threading, service detection, output formatting
#python3 port_scanner.py [METASPLOITABLE_IP] -p 1-10000
import socket 
import sys
import threading

class PortScanner:
    def __init__ (self, target, threads = 100):
        self.target = target
        self.threads = threads
        self.open_ports = []
        self.lock = threading.Lock()

        self.services = {
            21:"FTP", 22:"SSH", 23:"Telnet", 25:"SMTP", 53:"DNS",
            80:"HTTP", 110:"POP3", 139:"NetBIOS", 143:"IMAP", 443:"HTTPS",
            993:"IMAPS", 995:"POP3S", 3389:"RDP", 5432:"PostgreSQL", 3306:"MySQL"
        }

    def scan_port(self, port):
        print(f"scanning {self.target}:{port}...")
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            
            if result == 0:
                service = self.services.get(port, "unknown")
                with self.lock:
                    self.open_ports.append((port, service))
                    print(f"[+] port {port:5d} OPEN - {service}")
                
                
            sock.close()
        except Exception as e:
            pass
        
if __name__ == "__main__":
    scanner = PortScanner("127.0.0.1")
    scanner.scan_port(80)
    scanner.scan_port(443)
    print(f"found ports: {scanner.open_ports}")