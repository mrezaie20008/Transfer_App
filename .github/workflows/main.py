from socket import socket as sk, AF_INET, SOCK_STREAM

serv = sk(AF_INET, SOCK_STREAM)
serv.bind(("0.0.0.0", 12345))

client, _ = serv.accept()

print(client.recv(1024).decode())

serv.send("SC; BYE!".encode())

client.close()
serv.close()
