import os,sys,time
from socket import *

if __name__ == '__main__':
    PORT = 9889
    HOST = "127.0.0.1"
    sock = socket(AF_INET, SOCK_STREAM)

sock.bind((HOST, PORT))
sock.listen()
print("Listening on port " + str(PORT))

def recvall(sock):
    """
    Function to receive data from the given socket
    :param sock: connection of client
    :return: data sent by the client
    """

    BUFF_SIZE = 10  # 1 KiB
    data = b''
    while True:
        chunk = sock.recv(BUFF_SIZE)
        data += chunk
        if len(chunk) < BUFF_SIZE:
            # either 0 or end of data
            break
    return data


while True:
    clientSock, clientAddr = sock.accept()
    print("Connected to " + str(clientAddr))
    
    # Receive data from Client
    # Can we do better instead of hard coding it to 1024 bytes??
    data = clientSock.recv(1024)

    # data = recvall(conn)

    # Send data back to client
    clientSock.sendall(f"return data for id : {data.decode()}".encode())

    # Print the received data
    print(f"Address {clientAddr} \n Data: {data.decode()}")