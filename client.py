# Echo client program
import socket
import sys, os


HOST = '172.16.240.41'    # The remote host
PORT = 3000             # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))


try:
    while 1:
        try:
            c = sys.stdin.read(1)
            if c == 'quit':
            	print 'closing'
            	break
            else:
            	s.sendall(c)
        except IOError: pass
finally:
	s.close()
	print "closed"
