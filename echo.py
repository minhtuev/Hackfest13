# Echo server program
import socket, tester

#ip addr roombda: 172.16.241.70
#ip addr mac: 172.16.240.41
HOST = '172.16.240.41'    # Symbolic name meaning all available interfaces
PORT = 3000              # Arbitrary non-privileged port
motion = tester.ClientMotion()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

while 1:
	s.listen(1)
	conn, addr = s.accept()
	while 1:
		data = conn.recv(1024)

		if data == "quit":
			motion.flush()
			conn.close()
			print "closed socket"
			break
		else:
			motion.move(data)


