import socket

HOST = "127.0.0.1"  # todo: specify the server's hostname or IP address inside the quotes
PORT = 12345 # todo: specify the port number used by the server

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.connect((HOST, PORT))

    while True:
        message = input("Enter a message to send or type 'done' to quit")
        if message.lower() == 'done':
            print("Goodbye")
            break

    byte_msg = message.encode('utf-8')
    s.sendall(byte_msg)
    data = s.recv(1024)

print(f"Received: {data!r}".format(data.decode('utf-8')))