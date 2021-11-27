from ftplib import FTP
from ftplib import all_errors
from pythonping import ping
host = 'iele1400.ddns.net'
user = 'c_iele1400'
passwd = 'uniandes2020'

def callback(data):
    # print(data)
    f.write(data)

    p = ping(host, count = 1)
    for i in p: 
        i = str(i).split()[6][:-2]
        print(i)
        csv.write(i+'\n')

def download(filename):
    try:
        ftp = FTP( host,user, passwd)
        if ftp:
            global csv
            global f
            csv = open('ftp_{}_ping.csv'.format(filename), 'w')
            f = open("ftp_{}".format(filename), "wb")
        print(ftp.retrlines('LIST imagenes_proyecto_final'))
        ftp.cwd("imagenes_proyecto_final")
        ftp.retrbinary("RETR {}".format(filename), callback)
        csv.close()
        ftp.quit()
        f.close()
    except all_errors as e:
        print(e)
        ftp.quit()
        f.close()

def main():
    file = input("ingrese el nombre del archivo: ")
    download(file)
    pass

main()



