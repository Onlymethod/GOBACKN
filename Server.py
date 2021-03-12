import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print ( 'starting up on %s port %s' % server_address, sys.stderr)
sock.bind(server_address)
while True:
    print ('\n waiting to receive message', sys.stderr)
    data, address = sock.recvfrom(4096)
    print ('received %s bytes from %s' % (len(data), address), sys.stderr)
    print (data, sys.stderr)
    m = ord(data) + 1
    if data:
        sent = sock.sendto(chr(m), address)
        print ( 'sent %s bytes back to %s' % (sent, address), sys.stderr)
