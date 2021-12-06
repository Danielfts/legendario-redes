""" 
El código de referencia utilizado para desarrollar el funcionamiento básico de este código es el capítulo 2.7.2 
Socket programming with TCP del libro guía del curso, Computer Networking: A top Down Approach de James F. Kurose
y Keith W. Ross. 
Se utilizó la documentación oficial de las librerias utilizadas para aprender a utilizarlas. 
"""

import socket #Libreria importada para utilizar el socket
import os #Libreria importada para utilizar reportar excepciones
from pythonping import ping #Libreria importada para hsce un ping  

client_name = '0.0.0.0' #datos del cliente
client_port = 49809 #datos del cliente
server_name = 'iele1400.ddns.net' #datos del servidor 
server_port = 55555 #Datos del servidor

# png = ping(TCP_IP, size=1, count=1)
def descargar(archivo:str)->None: #funcion para descargar los archivos por socket 

    try: #es como un if, pero es para manejar de mejor manera los errores, previene errores 
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #aqui se define una instancia de objeto socket utilizando TCP-IP 
        client_socket.bind((client_name, client_port)) #se asocia el socket previamente creado a un puerto TCP (49809)
        client_socket.connect((server_name, server_port))#Se establece una conexion TCP con el servidor del proyecto.
        archivo_descarga = archivo.encode() #se toma el parametro archivo y se codifica en una variable con utf-8
        client_socket.send(archivo_descarga) #se envia el nombre del archivo codificado en la conexion TCP
        info = client_socket.recv(4096) #Se recibe la respuesta del servidor con la informacion proporcionada
        print(info) #se imprime la informacion
        if info: #condicion respecto a la informacion recibida 
            f = open('socket_{}'.format(archivo), 'wb') #se crea un archivo en el cliente para almacenar los paquetes
            csv = open('socket_{}_ping.csv'.format(archivo), 'w') #se crea un archivo para almacenar los datos de latencia. 
            while True: #bucle principal de descarga 
                data = client_socket.recv(4096) #en cada interacion se recibe un paquete con un buffer de 4096 Bytes
                p = str(ping(server_name, count = 1)._responses[0]).split() #Enviar un comando de ping al servidor. Tambien, se extrae la latencia en ms
                if len(p) == 7: #condicion para ignorar los timeouts del ping
                    p = p[6][:-2]
                    print(p)
                    csv.write(p+'\n') #escribe la latencia en un archivo csv 
                # print(data)
                if data == b'': #condicion para cerrar la conexion y los archivos cuando se termine la descarga
                    f.close()
                    csv.close
                    client_socket.close()
                    break
                else:
                    f.write(data)
                pass
            pass
        else: client_socket.close() #si no se recibe respuesta del servidor, cerrar el socket. 
        print(info)

    except os.error as e : #Manejo de excepciones por medio de la libreria OS para que el codigo pueda seguir funciondo. Informa al usuario del tipo de error
        print('lmao noob {}'.format(e)) #se burla del usuario e imprime el error


def main(): #Interfaz del programa. 
    while True:#Bucle principal de la interfaz 
        print("Interfaz de consola para hacer descargas por medio de sockets y tcp\n"
            "Daniel Felipe Triviño Santana y Yacob Andrés Lozano Espitia\n"
            "Fundamentos de Redes - 2021-2\n"
            "presione ctrl + c para salir del programa en cualquier momento")
        file = input("Ingrese el nombre del archivo que desea descargar: ") #recibe el nombre del archivo solicitado por el usuario. 
        print("-"*10)
        descargar(file) #descarga el archivo previamente configurado 

main() #Inicia el codigo. 