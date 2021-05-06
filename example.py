from src import WebServer,Request
from socket import socket
import signal
import sys

def shutdown(sing,unused):
    server.shutdown()
    sys.exit(1)

def index(request:Request,client:socket)->dict:
    if request.get_method=="GET":
        return {"data":"welcome to index page","type":"plain"}
    else:
        return {"data":"not protocol supported", "type": "plain"}

def programer(request:Request,client:socket)->dict:
    return {"data":"""<center>hello im hasan hk<br>
            You can follow me through my GitHub account<br>
            <img src=\"https://github.com/HSNHK.png?size=100\"><br>
            <a href=\"https://github.com/HSNHK\">GitHub Page</a>""", "type": "html"}

def fav(request: Request,client:socket) -> dict:
    file=open("fav.png","rb")
    return {"data":file.read(),"type":"img"}

signal.signal(signal.SIGINT, shutdown)

urlpatterns={"/":index,
    "/programer":[programer,"POST"],
    "/favicon.ico":fav}

server=WebServer(port=80,route=urlpatterns)
server.run()
