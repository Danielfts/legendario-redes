from socket import *

client_name = 'localhost'
client_port = 49809 
server_name = 'localhost'
server_port = 55554
client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.bind((client_name, client_port))

try:
    client_socket.connect((server_name, server_port))
    archivo_descarga = "800k.jpg".encode()
    
except :
    print('lmao noob')
    client_socket.close()

