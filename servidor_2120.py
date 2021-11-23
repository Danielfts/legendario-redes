# server2.py
#Universidad de los Andes
#Fundamentos de Redes IELE1400 - 202120

#Juan Pablo Castillo C.
#Dpto de Ingeniería Eléctrica y Electrónica
#Universidad de los Andes, Colombia

#El contenido de este script NO DEBE SER MODIFICADO este es solo de carácter ilustrativo
#Este mismo script corre en el servidor real
#No son válidas las pruebas realizadas en la máquina local, debe haber interacción con el servidor real.

#Véase la documentación explícita de cada línea.

#***Importación de librerías y módulos***
import socket
import os
from threading import Thread
from socketserver import ThreadingMixIn

#***Definición de constantes***

SEPARATOR = "<SEPARATOR>"   #Separador de caracteres para e envío de cadenas sencillas de texto.
TCP_IP = '0.0.0.0' #Parámetro para fijar dirección genérica en la configuración del socket. Es IP genérica pues no depende de otro servidor para responder.
TCP_PORT = 55555 #Puerto TCP de escucha (recepción de peticiones) en el servidor.
BUFFER_SIZE = 4096 #tamaño del buffer de empaquetamiento en máquina.

#***Definición de clases y funciones***

class ClientThread(Thread): #Clase que establece hilos de conexión con los clientes que envíen petición de enlace.

    def __init__(self,ip,port,sock): #Función  _init_ abre el socket e inicia un nuevo hilo de conexión (Función recusriva).
        Thread.__init__(self) #iniciar hilo
        self.ip = ip #almacenar dirección IP del cliente
        self.port = port #almacenar puerto TCP del cliente
        self.sock = sock # apertura del socket.
        print (" Nuevo hilo tendido para "+ip+":"+str(port)) #mensaje de confirmación

    def run(self): #Función run realiza el envío del mensaje solicitado de manera persistente utilizando el socket y el hilo abierto previamente.
        path=self.sock.recv(BUFFER_SIZE) #recibe el nombre(ruta) del archivo que el cliente desea obtener.
        cad = str(path).split("'") #Fragmenta la cadena recibida en las secciones útiles y crea un vector de almacenamiento.
        filename=cad[1] #selecciona el segundo elemento del vector creado previamente y lo almacena en la variable filename que contiene el nombre efectivo del archivo.
        print(filename) #muestra en consola el nombre del archivo solicitado por el cliente.
        #Búsqueda del archivo solicitado
        try:
            filesize = os.path.getsize(filename) #del nombre de archivo recibido (si existe) se obtine su tamaño en bytes.
            self.sock.send(f"{filename}{SEPARATOR}{filesize}".encode()) #al cliente se le retorna la información del archivo que ha solicitado.
            # Algoritmo de lectura y envío.
            with open(filename, "rb") as f:  # se abre el archivo solicitado en configuración read bytes.

                while True:  # se abre un while infinito.
                    bytes_read = f.read(
                        BUFFER_SIZE)  # en función del buffer de lectura de la máquina se lee el archivo y se almacena en una variable.
                    if not bytes_read:  # si no hay más información para leer, la transmisión debe terminar.
                        break  # break del while infinito (salida)
                    self.sock.sendall(
                        bytes_read)  # para garantizar el envío de toda la información incluso en redes congestionadas, se utiliza sendall() para crear una conexión persistente.
            self.sock.close()  # después del envío se cierra el socket
        except:
            self.sock.close() #si el archivo no existe se cierra la conexión el servidor envía respuesta incorrecta sobre la información del archivo.



#***Ejecucución de funciones***

tcpsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Creación del socket en cada hilo
tcpsock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #Parámetro de configuración del socket para permitir múltiples conexiones desde y hacia iguales direcciones.
tcpsock.bind((TCP_IP, TCP_PORT)) #Establecimiento de la dirección interna y puerto TCP de escucha.
threads = [] #Creación del vector de hilos.

while True: #El servidor funcionará de manera infinita
    tcpsock.listen(5) #para evitar un colapso del servicio, se aceptan 5 conexiones fallidas desde una dirección antes de rechazarla.
    print ("Esperando conexión de clientes...") #Mansaje de control en terminal
    (conn, (ip,port)) = tcpsock.accept() #Aceptación de conexiones de clientes en cada hilo
    print ('Conexión entrante desde ', (ip,port)) #Confirmación de conexión con cada cliente.
    newthread = ClientThread(ip,port,conn) #Definición de parámetros de un hilo nuevo
    newthread.start() #tendido de un nuevo hilo
    threads.append(newthread) #añadir el hilo creado recientemente al vector de hilos.

for t in threads: #recorrido por el  vector de hilos.
    t.join() #unir al proceso cada hilo dentro del vector.

# Fin del programa.