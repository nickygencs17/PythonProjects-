#import socket module

from socket import *

serverPort = 9445
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(("",serverPort))
serverSocket.listen(1)
while True:
    print "Ready to serve"
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        print filename,'||',filename[1:]
        f = open(filename[1:])
        outputdata =f.read()
        print outputdata
        connectionSocket.send("HTTP/1.1 200 OK\r\n\n")
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
        print "File Receieved"

    except IOError:
        connectionSocket.send('HTTP/1.1 404 File not found\r\n\n')
        connectionSocket.close()

serverSocket.close()
