import socket
import thread
import sys

def client_thread(connection):
try:
print >>sys.stderr, 'connection from', client_address

# Receive the data in small chunks and retransmit it
while True:
data = connection.recv(16)
print >>sys.stderr, 'received "%s"' % data
if data:
print >>sys.stderr, 'sending data back to the client'
connection.sendall(data)
else:
print >>sys.stderr, 'no more data from', client_address
break
  
finally:
# Clean up the connection
connection.close()
  
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(5)

while True:
# Wait for a connection
print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()
try:
thread.start_new_thread( client_thread, (connection, ) )
except:
print "Error: unable to start thread"

print "Exit the program"