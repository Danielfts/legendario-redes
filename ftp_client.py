from ftplib import FTP
host = 'iele1400.ddns.net'
user = 'c_iele1400'
passwd = 'uniandes2020'
ftp = FTP( 'localhost',user, passwd)

print(ftp.retrlines('LIST'))

ftp.quit()
