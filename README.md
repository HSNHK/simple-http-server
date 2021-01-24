# simple http server
In this project, it is supposed to be designed from the base of a http web server and it is just a small example.<br>
This project is designed in Python language.<br>
It may become a flask-like library in the future<br>

A simple example : 
```python
import web_server

def index()->dict:
    return {"data":"hello welcome to my site","type":""}
    
def favicon()->dict:
    file=open("favicon.png",'rb')
    return {"data":file.read(),"type":"img"}
    
urlpatterns={
    "/":index,
    "/favicon.ico":favicon
}

server=web_server(port=8080,route=urlpatterns)
server.start()
```
