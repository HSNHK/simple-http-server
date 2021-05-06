from .io import Response,Request
from datetime import datetime
from logging import DEBUG
from .log import Log
import threading
import socket
import sys

class WebServer:
    def __init__(self,host="127.0.0.1",port=8080,route={},DEBUG=False):
        self.HOST=host
        self.PORT=port
        self.route_table=route
        if DEBUG:
            self.Log=Log(Name="Server logging",level=DEBUG)
        else:
            self.Log=Log("Server logging")
        print("* Welcome to the web server\n" \
              "* debug mode : ",DEBUG)
        
    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind((self.HOST,self.PORT))
            self.Log.info("*Start Webserver with :%s:%s "%(self.HOST,self.PORT))
        except:
            self.Log.critical("Difficult to run. This port is probably reserved")
            self.shutdown()

        self.__listen()

    def shutdown(self):
        self.socket.shutdown(socket.SHUT_RDWR)
        sys.exit(1)

    def __listen(self):
        self.socket.listen(5)
        try:
            while True:
                (client,address)=self.socket.accept()
                client.settimeout(60)
                self.Log.info("connect new client Host : %s Port : %d"%(address[0],address[1]))
                threading.Thread(target=self.__handling,args=(client,address)).start()
        except Exception as ex:
            self.Log.error("server listen error : %s"%ex)

    def __send(self,request,header:str,data:str):
        response=header.encode()
        response+=data
        request.send(response)
        request.close()

    def __handling(self,client,addres):
        PACKET_SIZE=1024
        while True:
            try:
                data = client.recv(PACKET_SIZE).decode()

                if not data:
                    break
                request=Request(data)

                self.Log.info("The request: |%s| |%s| |%s| |%s|"%("{}:{}".format(addres[0],addres[1]),
                                request.get_method,
                                request.get_parameter,
                                str(datetime.now())))

                if request.get_parameter in self.route_table:
                    if type(self.route_table[request.get_parameter]) is list:
                        Method=self.route_table[request.get_parameter][1]
                        if request.get_method.casefold()!=Method.casefold():
                             self.protocol_not_supported(client)
                             break
                        function=self.route_table[request.get_parameter][0](request,client)
                    else:
                        function=self.route_table[request.get_parameter](request,client)

                    DATA=function["data"]
                    if type(DATA)!=bytes:
                        DATA=str(DATA).encode()

                    HEADER=Response(status_code=200,content_type=function["type"])
                    self.__send(client,HEADER.generate_header(),DATA)
                    break
                else:
                    self.not_found(client)
                    break
            except Exception as ex:
                self.Log.error("Internal Server Error : ",ex)
                self.internal_error(client)
                break
    
    def not_found(self,client):
        HEADER = Response(status_code=404, content_type="html")
        self.__send(client, HEADER.generate_header(),
                    "<br>Not Found 404</br>".encode())

    def internal_error(self,client):
        HEADER = Response(status_code=500, content_type="html")
        self.__send(client, HEADER.generate_header(),
                    "<h1>Internal Server Error 500</h1>".encode())

    def protocol_not_supported(self,client):
        HEADER = Response(status_code=404, content_type="html")
        self.__send(client, HEADER.generate_header(),
                    "<br>Protocol Not Supported</br>".encode())
