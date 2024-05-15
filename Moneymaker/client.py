import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

while True:
    command = input("Enter command (increment/decrement): ").strip()
    if command == "quit":
        break
    client_socket.send(command.encode())
    response = client_socket.recv(1024).decode()
    print("Response from server:", response)

client_socket.close()
