import dht_operations as dht
import socket
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create TCP/IP
s.bind((socket.gethostname(), 42069)) #bind the socket to host IP and specify a port
s.listen(5)

while True:
    clientsocket, address = s.accept()

