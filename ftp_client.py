from ftplib import FTP
import os
host = 'iele1400.ddns.net'
user = 'c_iele1400'
passwd = 'uniandes2020'

def callback(data):
    print(data)
    f.write(data)

def download(filename):
    try:
        ftp = FTP( host,user, passwd)
        if ftp:
            global f
            f = open(filename, "wb")
        print(ftp.retrlines('LIST imagenes_proyecto_final'))
        ftp.cwd("imagenes_proyecto_final")
        ftp.retrbinary("RETR {}".format(filename), callback)
        ftp.quit()
        f.close()
    except os.error as e:
        print(e)
        ftp.quit()
        f.close()

download("800k.jpg")

