import socket, sys
from _thread import *

server = "10.0.2.15"
port = 8091
numConnections = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(s)

s.listen(2)
print("Server started, waiting for connection")

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)
            conn.sendall(str.encode(reply))
        except:
            break
    print("Lost connection")
    global numConnections
    numConnections -= 1
    conn.close()

while True:
    if numConnections <= 8:
        conn, addr = s.accept()
        print("Connected to: ", addr)
        numConnections += 1
        start_new_thread(threaded_client, (conn,))
    else:
        print("Max connections reached")
    print("Active connections: ", numConnections)