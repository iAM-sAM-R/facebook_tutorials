import socket
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("192.168.1.14", 9999))
server.listen(5)

print("awaiting connection")

while True:
    client, address = server.accept()
    print("Connected to host", address)
    
    
    while True:

        i = 0
        
        print("Green. Cars can go.")
        
        while True:
            client.send(bytes("Green", "utf-8"))
            time.sleep(.5)
            i = i + 1
            if i == 10:
                i = 0
                break            
        
        print("Yellow. Cars should slow down.")        
        while True:
            client.send(bytes("Yellow", "utf-8"))
            time.sleep(.5)
            i = i + 1
            if i == 6:
                i = 0
                break
        
        print("Red. Cars must stop.")
        
        while True:
            client.send(bytes("Red","utf-8"))
            time.sleep(.5)
            i = i + 1
            if i == 10:
                i = 0
                break
