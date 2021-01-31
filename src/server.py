from .header import Generate,Assembler
from datetime import datetime
from logging import DEBUG
from .log import Log
import threading
import socket
import sys

class web_server:
    def __init__(self,host="127.0.0.1",port=8080,route={},DEBUG=False):
        self.HOST=host
        self.PORT=port
        self.route_table=route
        if DEBUG:
            self.Log=Log(Name="Server logging",level=DEBUG)
        else:
            self.Log=Log("Server logging")
        print("* Welcome to the web server\n" +
              "* debug mode : ",DEBUG)
        
    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.socket.bind((self.HOST,self.PORT))
            self.Log.info(message="Start Webserver with :%s:%s "%(self.HOST,self.PORT))
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
                self.Log.info(message="connect new client Host : %s Port : %d"%(address[0],address[1]))
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
                request_data=Assembler(data)

                self.Log.info("The request: |%s| |%s| |%s| |%s|"%("{}:{}".format(addres[0],addres[1]),
                                request_data.get_method,
                                request_data.get_parameter,
                                str(datetime.now())))

                if request_data.get_parameter in self.route_table:
                    function=self.route_table[request_data.get_parameter](request_data)
                    DATA=function["data"]
                    HEADER=Generate(status_code=200,content_type=function["type"])
                    self.__send(client,HEADER.generate_header(),DATA)
                    break
                else:
                    HEADER=Generate(status_code=404)
                    self.__send(client,HEADER.generate_header(),"<br>Not Found 404</br>".encode())
                    break
            except Exception as ex:
                self.Log.error("Internal Server Error : "+ex)
                HEADER=Generate(status_code=500)
                self.__send(client, HEADER.generate_header(),
                            "<h1>Internal Server Error 500</h1>".encode())
                break

