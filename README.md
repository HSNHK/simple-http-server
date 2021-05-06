# simple http server
In this project, it is supposed to be designed from the base of a http web server and it is just a small example.<br>
# Life cycle
```
ServerBuilder -> Accept -> WorkerClient -> Worker -> Dispatcher
```
## Simple example
```python

from src import WebServer,Request


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
    
urlpatterns = {"/":index,
    "/programer":[programer,"POST"],
    "/favicon.ico":fav}

server=WebServer(port=80,route=urlpatterns)
server.run()

```
# Request
```python
# Type of request method received
request.get_method
# url parameter
request.get_parameter
# http version
request.get_http_version
# client host info
request.get_host
# connection status
request.get_connection
# content len
request.get_content_length
# client user agent
request.get_user_agent
# request content type
request.get_content_type
# body
request.get_body
```