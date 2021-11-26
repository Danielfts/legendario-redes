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
            f = open('socket_{}'.format(archivo), 'wb')
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
        else: client_socket.close()
        print(info)

    except os.error as e :
        print('lmao noob {}'.format(e))


def main():
    while True:
        print("Interfaz de consola para hacer descargas por medio de sockets y tcp\n"
            "Daniel Felipe Triviño Santana y Yacob Andrés Lozano Espitia\n"
            "Fundamentos de Redes - 2021-2\n"
            "presione ctrl + c para salir del programa en cualquier momento")
        file = input("Ingrese el nombre del archivo que desea descargar: ")
        print("-"*10)
        descargar(file)

main()
