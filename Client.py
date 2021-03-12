import socket
import sys

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 10000)
message = '0'
#'This is the message.  It will be repeated.'
try:
	
    # Send data
		print ('sending "%s"' % message, file=sys.stderr)
		sent = sock.sendto(message, server_address)

    # Receive response
		print ('waiting to receive', sys.stderr)
		data, server = sock.recvfrom(4096)
		
		print >>sys.stderr, 'I have to send "%s"' % data
		while str(data) != '9':
		
			message = data
			
			sent = sock.sendto(message, server_address)
		    
			data, server = sock.recvfrom(4096)
		
			print ('I have to send "%s"' % data, sys.stderr)
		
			

finally:
    print ('closing socket', sys.stderr)
raw_input()
sock.close()
