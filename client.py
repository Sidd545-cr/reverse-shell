import subprocess
import socket





def client():
    Socket = socket.socket()
    host = socket.gethostname()
    port = 52274
    
    Socket.connect((host, port))
    msg=""
    while(msg!="quit"):
        msg = input("[+] Enter command: ") 
        if (msg == ""):
            continue
        data = Socket.send(msg.encode())
        print("msg sent from client")
        output=Socket.recv(1024)
        print("msg recieved from server")
        print(output.decode().strip("\r\n"))
    Socket.close()



client()
