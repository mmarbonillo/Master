import socket

#my_socket = socket.socket(socket_family,socke_type, protocolo)
#socket_family = familia de protocolos usada como mecanimos de transporte - AF_INET, PF_INET, PF_UNIX, PF_X25
#socket_type = tipo de comunicacion entre los 2 extrmos - SOCK_STREAM  (protocolo orientados a conexiones ) y SOCK_DGRAM (protocolo sin conexiones)
#protocolo = 0

host = socket.gethostname()
port = 12345
BUFFER_SIZE = 1024

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as socket_tcp:
    
    socket_tcp.bind((host,port))
    socket_tcp.listen(5)
    conn, addr = socket_tcp.accept()
    with conn:
        print("Conexión establecida")
        data = conn.recv(BUFFER_SIZE)
        if not data:
            print("No hay datos")
        else:
            print("Datos recibidos {}".format(data.decode('utf-8')))
            conn.send(data)