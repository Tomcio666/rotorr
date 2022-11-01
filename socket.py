from email import message
import socket


def server():
    host = socket.gethostname()
    port = 5000

    server_soc = socket.socket()
    print("udalo sie")

    server_soc.bind(host,port)
    print("socket bind do %s" %(port))

    server_soc.listen(1)
    print("socket slucha")

    while True:
        conn, adress = server_soc.accept()
        print("connction z: "+str(adress))
        data = conn.recv(1024).decode()
        
        if not data:
            break

        message = "rotating to rotor " + data
        conn.send(message.encode())

    conn.close()


if __name__ == '__main__':
    server() 

    