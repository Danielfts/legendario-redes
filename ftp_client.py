""" 
 Para desarrollar este código sólo se hizo uso de la documentación oficial de las librerias de python utilizadas. 
 """
from ftplib import FTP #Libreria fundamental, facilita utilizar FTP con python 
from ftplib import all_errors
from pythonping import ping
import os
host = 'iele1400.ddns.net' #asignacion de variable
user = 'c_iele1400'#asignacion de variable
passwd = 'uniandes2020'#asignacion de variable

def callback(data): #en esta funcion se define lo que uno quiere/puede hacer con los paquetes que llegan
    # print(data)
    f.write(data) #escribe los datos recibidos en binario en el archivo f

    p = str(ping(host, count = 1)._responses[0]).split() #llama la funciion ping una sola vez para extraer el dato de latencia.
    if len(p) == 7: #esta estructura se usa para ignorar los timeouts del ping
        p = p[6][:-2]
        print(p)
        csv.write(p+'\n')

def download(filename): #usa como parametro el nombre ingresado en def main()
    try: #es como un if, pero es para manejar de mejor manera los errores, previene errores
        ftp = FTP( host,user, passwd) #es una instancia de objeto ftp, con parametros como host, user, password; estos tres parametros se definieron el las lineas 5,6,7
        #en la linea de arriba, se define a "ftp" para crear un elemento especifico basado en FTP y los parametros dados
        if ftp: #se genera una condicion en donde se pone a prueba la existencia de la variable creada anteriormente. 
            global csv #global ayuda a que esta variable se pueda usar fuera de esta funcion
            global f #global ayuda a que esta variable se pueda usar fuera de esta funcion
            csv = open('ftp_{}_ping.csv'.format(filename), 'w') #aca se crea la variable para guardar los datos hechos por el ping o tambien llamados de latencia
            f = open("ftp_{}".format(filename), "wb") #en esta variable se crea un archivo binaRIO para almacenar los archivos recibidos por FTP
            print(ftp.retrlines('LIST imagenes_proyecto_final')) #esta linea muestra los archivos que hay en el directorio raiz del servidor 
            ftp.cwd("imagenes_proyecto_final") # "change work directory" cambia el directorio a la carpeta seleccionada que es donde estan los archivos que buscamos.
            ftp.retrbinary("RETR {}".format(filename), callback) #LINEA MAS IMPORTANTE DEL CODIGO: Solicita al servidor que envie el archivo dado por el parametro filename en binario. 
            #Así mismo, callback se usa cada vez que llega un paquete y se define en la funcion "callback". 
            csv.close() #cierra el archivo csv
            ftp.quit() #cierra la conexion ftp 
            f.close() #cierra el archivo en el que se almacena la descarga 
    except all_errors as e: #se hace una implementacion de la libreria para manejar las excepciones mas comunes de FTP
        print(e) #imprime el error 
        ftp.quit() #cierra la conexion ftp
        f.close() #cierra el arvchivo en el que se almacena la descarga

def main(): # recibe el nombre del archivo y llama la funcion principal
    file = input("ingrese el nombre del archivo: ")
    download(file)
    pass

main()
