from src import web_server,Assembler
import signal
import sys

def shutdown(sing,unused):
    server.shutdown()
    sys.exit(1)

def index(request:Assembler)->dict:
    if request.get_method=="GET":
        return {"data":b"welcome to index page","type":"plain"}
    else:
        return {"data": b"not protocol supported", "type": "plain"}

def programer(request:Assembler)->dict:
    return {"data":b"""<center>hello im hasan hk<br>
            You can follow me through my GitHub account<br>
            <img src=\"https://github.com/HSNHK.png?size=100\"><br>
            <a href=\"https://github.com/HSNHK\">GitHub Page</a>""", "type": "html"}

def fav(request: Assembler) -> dict:
    file=open("fav.png","rb")
    return {"data":file.read(),"type":"img"}

signal.signal(signal.SIGINT, shutdown)

urlpatterns={"/":index,
    "/programer":programer,
    "/favicon.ico":fav}

server=web_server(port=80,route=urlpatterns)
server.run()
