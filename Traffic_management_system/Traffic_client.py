import socket
import time


while True:
    # create socket
    client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host_ip = '192.168.1.14'
    port = 9999
    client_socket.connect((host_ip,port))
    
    while True:
        try:
            text = client_socket.recv(1024)
            print(text.decode())
            if len(text) == 0:
                raise Exception
        except:
            break
    
    client_socket.close()
    
    
import msvcrt as m
m.getch()
