import socket
import sys
from datetime import datetime
import threading
import signal
import json


class web_server:
    def __init__(self,port=8080,route={}):
        self.HOST="127.0.0.1"
        self.PORT=port
        self.route_table=route
    def start(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind((self.HOST,self.PORT))
            print("Start Webserver with :%s:%s "%(self.HOST,self.PORT))
        except:
            print("Difficult to run\nThis port is probably reserved")
            self.shutdown()

        self.listen()

    def shutdown(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        sys.exit(1)

    def generate_headers(self,status_code,contentType):
        header=""
        if status_code==200:
            header+="HTTP/1.1 200 OK\n"
        elif status_code==404:
            header+="HTTP/1.1 404 Not Found\n"
            
        header+="Access-Control-Allow-Origin: *\n"
        header+="Access-Control-Allow-Headers: Content-Type, Set-Cookie, *\n"
        header+="Set-Cookie: session=344772952; Domain=0.0.0.0; expires=Fri, 19-Jan-2018 20:04:36 PST; Path=/\n"
        
        header+="Date :%s\n"%datetime.now()
        header+="Server :First webserver\n"

        if contentType=="json":
            header+="Content-type :application/json\n"
        elif contentType=="img":
            header += "Content-type :image/png\n"
        else:
            header += "Content-type :text/plain\n"

        header+="Connection :close \n\n"

        return header
    
    def listen(self):
        self.socket.listen(5)
        try:
            while True:
                (client,address)=self.socket.accept()
                client.settimeout(60)
                print("connect new client %s",address)
                threading.Thread(target=self.handling,args=(client,address)).start()
        except Exception as ex:
            print(ex)

    def handling(self,client,addres):
        PACKET_SIZE=1024
        while True:
            data = client.recv(PACKET_SIZE).decode()

            if not data:
                break

            request_data=data.split(' ')
            print("request method : %s"%request_data[0])
            if request_data[1] in self.route_table:
                func=self.route_table[request_data[1]]()
                response_data=func["data"]
                response=self.generate_headers(200,func["type"]).encode()
                response+=response_data
                client.send(response)
                client.close()
                break
            else:
                response_data="not found"
                response=self.generate_headers(404,"").encode()
                response+=json.dumps(response_data).encode()
                client.send(response)
                client.close()
                break

def shutdown(sing,unused):
    server.shutdown()
    sys.exit(1)

def index()->dict:
    return {"data":b"index ...","type":""}

def programer()->dict:
    return {"data":b"hello im hasan hk","type":""}

def fav()->dict:
    file=open("922844.png","rb")
    return {"data":file.read(),"type":"img"}

signal.signal(signal.SIGINT, shutdown)

urlpatterns={"/":index,
    "/programer":programer,
    "/favicon.ico":fav}
server=web_server(port=8081,route=urlpatterns)
server.start()

