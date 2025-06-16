"""port scanner for cybersec learning
features: multi threading, service detection, output formatting"""

import socket 
import sys

services = {
    21:"", 22:"SSH", 23:"Telnet", 25:"SMTP", 53:"DNS",
    80:"HTTP", 110:"POP3", 139:"NetBIOS", 143:"IMAP", 443:"HTTPS",
    993:"IMAPS", 995:"POP3S", 3389:"RDP", 5432:"PostgreSQL", 3306:"MySQL"
}

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0
    except Exception as e:
        return False
    
if __name__ == "__main__":
    result = scan_port("127.0.0.1", 22)
    print(f"result: {result}")