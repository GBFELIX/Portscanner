import sys
import socket
from datetime import datetime

x = int(input("Primeira porta a ser escaneada"))
y = int(input("ultima porta a ser escaneada"))
target = input("digite o alvo a ser escaneado")

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #traduz de hostname pra ipv4
else:
    print("numero de argumentos errados ou sintase errada")
    print("hot to exe (python portscan.py <ip>)")

#desing
print("-" * 50)
print("scanneando: " +target)
print("inicio: " +str(datetime.now()))
print("-" * 50)

try: 
    for port in range(x,y):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print(f"port {port} esta aberta")
        s.close()
except KeyboardInterrupt:
    print("\nFechando programa")
    sys.exit()
except socket.gaierror:
    print("hostname bugou D:")
    sys.exit()
except socket.error:
    print("nao conseguiu acesso ao servidor")