# Echo server program
import socket, tester

HOST = '172.16.240.41'                 # Symbolic name meaning all available interfaces
PORT = 3000              # Arbitrary non-privileged port
motion = tester.ClientMotion()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)
conn, addr = s.accept()
print 'Connected by', addr
while 1:
    data = conn.recv(1024)
    motion.move(data)
    if data == "p":
    	break
    if not data: 
    	break
    conn.sendall(data)
conn.close()