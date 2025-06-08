from socket import socket as sk, AF_INET, SOCK_STREAM
from requests import get

# IP Reveal
print(f"IP: {get("https://api.ipify.org").text}")

# Server Code
serv = sk(AF_INET, SOCK_STREAM)
serv.bind(("0.0.0.0", 12345))

client, _ = serv.accept()

print(client.recv(1024).decode())

serv.send("SC; BYE!".encode())

client.close()
serv.close()
