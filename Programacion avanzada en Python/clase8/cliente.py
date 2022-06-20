import socket

host = socket.gethostname()
port = 12345
MENSAJE = "Hola mundo"

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket_tcp:
    socket_tcp.connect((host,port))
    socket_tcp.send(MENSAJE.encode('utf-8'))
    data = socket_tcp.recv(1024)
    print(data)