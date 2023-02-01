import sys,os,time,socket


def send_message(message):
    """
    Function to communicate with the server.
    :param message: Message you would like to send the server
    """

    s = socket.socket()
    s.connect((HOST, PORT))
    print("Connected on port " + str(PORT) + " to address " + HOST)
    s.sendall(message.encode())
    data = s.recv(1024)
    print(f"{data.decode()}")
    s.close()
    pass


if __name__ == '__main__':
    # Defining the server address
    HOST = "127.0.0.1"
    PORT = 9889

    for i in range(1, 10):
        send_message(f"Test message id {i}")