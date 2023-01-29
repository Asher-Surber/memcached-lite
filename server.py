import os,sys,time
from socket import *

PORT = 9889
HOST = "127.0.0.1"
sock = socket.socket(AF_INET, SOCK_STREAM)

sock.bind(HOST, PORT)
sock.listen()
print("Listening on port " + PORT)

while True:
    clientSock, clientAddr = sock.accept()
    print("Connected to {clientAddr}")
    