from header import StatusCode,ContentTypes
from datetime import datetime

class generate():
    def __init__(self, version=1.1, status_code=200, content_type="plain"):
        self.code=StatusCode()
        self.type=ContentTypes()

        self.content_type=content_type
        self.header="HTTP/1.1 "
        self.date=datetime.now()
        self.server_name="http server by HSNHK"
        self.status_code=status_code

    def set_date(self,date=datetime.now):
        self.date=datetime.now()

    def set_server_name(self,name):
        self.server_name=name
    
    def set_content_type(self,type):
        self.content_type=self.type.get(type)

    def set_status_code(self,code):
        self.status_code=code

    def generate_header(self)->str:
        self.header+="%d %s\n"%(self.status_code,self.code.get(self.status_code))
        self.header+="Date : %s\n"%self.date
        self.header+="Server : %s\n"%self.server_name
        self.header+="Content-type : %s\n" %self.content_type
        self.header+="Connection : close\n\n"
        return self.header

