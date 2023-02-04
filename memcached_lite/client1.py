from socket import *

HOST = "127.0.0.1"
PORT = 9889
sock = socket(AF_INET, SOCK_STREAM)


def send_request(request):
    sock.connect((HOST, PORT))
    print("Connected on port " + str(PORT) + " to address " + HOST)
    sock.sendall(request.encode())
    data = sock.recv(1024)
    print(f"{data.decode()}")
    sock.close()



while True:
    requestType = input("Get or Set? ")
    if(requestType.lower() == "get"):
        key = input("Key: ")
        request = f"get {key}\r\n"
        send_request(request)
    elif(requestType.lower() == "set"):
        key = input("Key: ")
        value = input("Value: ")
        valSize = len(value)
        request = f"set {key} {valSize} \r\n{value} \r\n"
        send_request(request)
    else:
        print("Invalid command")