import os,sys,time
from socket import *

if __name__ == '__main__':
    PORT = 9889
    HOST = "127.0.0.1"
    sock = socket(AF_INET, SOCK_STREAM)

sock.bind((HOST, PORT))
sock.listen()
print("Listening on port " + str(PORT))


if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
    PATH_DELIM = "/"

elif sys.platform.startswith("win32"):
    PATH_DELIM = "\\"

else:
    print("unsupported platform, file path errors possible")
    PATH_DELIM = "/"


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




with open(os.curdir + PATH_DELIM + "data.txt", "r+", encoding="utf-8") as f:

    def get(key):
        lines = f.readlines()
        for l in lines:
            if l.startswith(key):
                val = l.partition(" ")[2]
                return f"VALUE {key} {len(val)} \r\n{val}\r\n"

    def set(key, value):
        lines = f.readlines()
        for l in lines:
            if l.startswith(key):
                l = value
                try:
                    f.writelines(lines)
                    return "STORED\r\n"
                finally:
                    return "NOT-STORED\r\n"
        lines.append(key + " " + value)
        try:
            f.writelines(lines)
            return "STORED\r\n"
        finally:
            return "NOT-STORED\r\n"



    while True:
        clientSock, clientAddr = sock.accept()
        print("Connected to " + str(clientAddr))
        
        # Receive data from Client

        data = recvall(clientSock)
        dataStr = data.decode()

        # parse data, decide what course of action to take, either retrieve, store, or send error

        if dataStr.startswith("get"):
            tmp = dataStr.split(" ")
            key = tmp[1]
            response = get(key)
        
        elif dataStr.startswith("set"):
            tmp1 = dataStr.split("\r\n")
            line1 = tmp1[0].split(" ")
            line2 = tmp1[1].split(" ")

            key = line1[1]
            valSize = line1[2]
            val = line2[0]
            response = set(key, val)

        else:
            response = "Invalid command"

        # Send data back to client
        clientSock.sendall(response.encode())
        clientSock.sendall("END\r\n".encode())

        # Print the received data
        print(f"Address {clientAddr} \n Data: {data.decode()}")