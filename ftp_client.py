from ftplib import FTP
ftp = FTP('iele1400.ddns.net','c_iele1400', 'uniandes2020')
print(ftp.retrlines('LIST'))

ftp.quit()
