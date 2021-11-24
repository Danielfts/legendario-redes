import socket
import os
client_name = '0.0.0.0'
client_port = 49809
server_name = 'iele1400.ddns.net'
server_port = 55555
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind((client_name, client_port))

def descargar(archivo:str)->None:   

    try:
        client_socket.connect((server_name, server_port))
        archivo_descarga = archivo.encode()
        client_socket.send(archivo_descarga)
        info = client_socket.recv(4096)
        if info:
            f = open('download.jpg', 'wb')
            while True:
                data = client_socket.recv(4096)
                print(data)
                if data == b'':
                    f.close()
                    client_socket.close()
                    break
                else:
                    f.write(data)
                pass
            pass
        print(info)

    except os.error as e :
        print('lmao noob {}'.format(e))
        client_socket.close()

descargar('800k.jpg')