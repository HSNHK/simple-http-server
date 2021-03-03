# simple http server
In this project, it is supposed to be designed from the base of a http web server and it is just a small example.<br>
This project is designed in Python language.<br>
It may become a flask-like library in the future<br><br>
The image below illustrates the transfer of requests:<br>
<img src="https://raw.githubusercontent.com/HSNHK/simple-http-server/main/doc/Description.png" width="500" height="300">
## simple example : 
```python

import web_server

def index(request:Assembler)->dict:
    if request.get_method=="GET":
        return {"data":b"welcome to index page","type":"plain"}
    else:
        return {"data": b"not protocol supported", "type": "plain"}
    
def fav(request: Assembler) -> dict:
    file=open("fav.png","rb")
    return {"data":file.read(),"type":"img"}
    
urlpatterns={"/":index,
    "/programer":programer,
    "/favicon.ico":fav}

server=web_server(port=8080,route=urlpatterns)
server.start()

```
The example above is an example of using this library<br>
Each function must have a dict output<br>
*data Output data : (type : Binary , value : * )<br>
*type Output data type : (type : String , value : Content Types )<br>

## Content Types

css  : text/css<br>
csv  : text/csv<br>
html : text/html<br>
php  : text/php<br>
plain: text/plain<br>
xml  : text/xml<br>
git  : image/gif<br>
apng : image/apng<br>
flig : image/flif<br>
webp : image/webp<br>
x_mng: image/x-mng<br>
jpeg : image/jpeg<br>
png  : image/png<br>
json : application/json<br>
## Server reports
<img src="https://raw.githubusercontent.com/HSNHK/simple-http-server/main/doc/Log.JPG" width="700" height="200"><br><br>
<p><img src="https://github.com/HSNHK.png?size=50"><a href="https://github.com/HSNHK"> By🧡HSNHK</a></p><br>


