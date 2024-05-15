import socket
import threading
import time

shared_variable = 0
lock = threading.Lock()

def modify_variable(value):
    global shared_variable
    with lock:
        shared_variable += value
    time.sleep(0.5)

def handle_user(conn, addr):
    print(f"User connected: {addr}")
    try:
        while True:
            data = conn.recv(1024).decode().strip()
            if not data:
                break
            if data == "increment":
                copy =  shared_variable
                modify_variable(1)
            elif data == "decrement":
                copy = shared_variable
                modify_variable(-1)
            elif data == "quit":
                break
            else:
                conn.send(b"Invalid command\n")
                continue
            if shared_variable == copy:
                conn.send(b"Flag: SECSOC{vrooom}\n")
            conn.send(f"Current is {shared_variable} was {copy}\n".encode())
    finally:
        print(f"User disconnected: {addr}")
        conn.close()

def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server listening on port 12345...")
    while True:
        conn, addr = server_socket.accept()
        thread = threading.Thread(target=handle_user, args=(conn, addr))
        thread.start()

server_thread = threading.Thread(target=server)
server_thread.start()
