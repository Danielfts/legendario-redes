from ftplib import FTP
servidor = "31.170.164.144"
user="u133550882"
passw="12345asd"

try:
    conexion = FTP(servidor)
    conexion.login(user,passw)
    print("Conexion estable")
except Exception:
    print("No se pudo establecer la conexion al servidor")

conexion.retrlines("LIST")

fich= open("Prueba_servidorFTP.txt", "wb")
conexion.retrbinary("RETR Prueba_servidorFTP.txt", fich)
fich.close()

conexion.quit()