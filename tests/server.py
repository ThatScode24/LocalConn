import socket 
import threading
from datetime import datetime
import os
import shutil

HEADER = 64
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)


def handle_client(conn, addr):
    #to get nickname as first message
    nickname_length = conn.recv(HEADER).decode()
    if nickname_length:
        nickname_length = int(nickname_length)
        nickname = conn.recv(nickname_length).decode(FORMAT)
        now = datetime.now()
        time = now.strftime("%H:%M:%S")
        print(f"[{time}]: {nickname}({addr[0]}) connected")

        with open(f'{nickname}-info.txt', "wb") as file:
            print("Retrieving client info...")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                file.write(data)
    connected = True
    #then listen for other messages

    while connected:
        try:
            msg_length = conn.recv(HEADER).decode()
            if msg_length:
                msg_length = int(msg_length)
                msg = conn.recv(msg_length).decode(FORMAT)
                if msg == DISCONNECT_MESSAGE:
                    connected = False
                print(f"[{addr}]: {msg}")
        except:
            pass
    

def start():
    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() -  1}")

print(f"[{SERVER}]: Server starting on port {PORT}")
start()