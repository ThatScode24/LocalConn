import socket

PORT = 5050


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def conn(addr):
    client.connect((addr, 5050))