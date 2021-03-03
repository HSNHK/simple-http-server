from src import web_server,Assembler
import signal
import sys

def shutdown(sing,unused):
    server.shutdown()
    sys.exit(1)

def index(request:Assembler,client)->dict:
    if request.get_method=="GET":
        return {"data":"welcome to index page","type":"plain"}
    else:
        return {"data":"not protocol supported", "type": "plain"}

def programer(request:Assembler,client)->dict:
    return {"data":"""<center>hello im hasan hk<br>
            You can follow me through my GitHub account<br>
            <img src=\"https://github.com/HSNHK.png?size=100\"><br>
            <a href=\"https://github.com/HSNHK\">GitHub Page</a>""", "type": "html"}

def fav(request: Assembler,client) -> dict:
    file=open("fav.png","rb")
    return {"data":file.read(),"type":"img"}

signal.signal(signal.SIGINT, shutdown)

urlpatterns={"/":index,
    "/programer":[programer,"POST"],
    "/favicon.ico":fav}

server=web_server(port=80,route=urlpatterns)
server.run()
