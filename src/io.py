from datetime import datetime

class ContentTypes():
    def __init__(self):
        self.__type = {
            "css": "text/css",
            "csv": "text/csv",
            "html": "text/html",
            "php": "text/php",
            "plain": "text/plain",
            "xml": "text/xml",
            "git": "image/gif",
            "apng": "image/apng",
            "flig": "image/flif",
            "webp": "image/webp",
            "x_mng": "image/x-mng",
            "jpeg": "image/jpeg",
            "png": "image/png",
            "json": "application/json"
        }

    def get(self, type) -> str:
        return self.__type[type]

    def add(self, name: str, content: str):
        self.__type[name] = content

    def delete(self, type: str):
        del self.__type[type]


class StatusCode():
    def __init__(self):
        self.__status_code = {
            200: "OK",
            201: "Created",
            202: "Accepted",
            203: "Non-Authoritative Information",
            204: "No Content",
            205: "Reset Content",
            305: "Use Proxy",
            400: "Bad Request",
            401: "Unauthorized",
            403: "Forbidden",
            404: "Not Found",
            405: "Method Not Allowed",
            406: "Not Acceptable",
            408: "Request Timeout",
            500: "Internal Server Error",
            501: "Not Implemented",
            502: "Bad Gateway",
            503: "Service Unavailable",
            504: "Gateway Timeout",
            505: "HTTP Version Not Supported"
        }

    def get(self, code) -> str:
        return self.__status_code[code]

    def add(self, code: int, content: str):
        self.__status_code[code] = content

    def delete(self, code: int):
        del self.__status_code[code]

class Response:
    def __init__(self, version=1.1, status_code=200, content_type="plain"):
        self.code=StatusCode()
        self.type=ContentTypes()

        self.content_type=self.type.get(content_type)
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

class Request:
    def __init__(self,header:str):
        self.__header_Assembled=header.splitlines()

    @property
    def get_method(self)->str:
        return self.__header_Assembled[0].split(' ')[0]

    @property
    def get_parameter(self)->str:
        return self.__header_Assembled[0].split(' ')[1]

    @property
    def get_http_version(self)->str:
        return self.__header_Assembled[0].split(' ')[2]
    
    @property
    def get_host(self)->str:
        return self.__header_Assembled[1].split(':')[1].strip()

    @property
    def get_connection(self)->str:
        return self.__header_Assembled[2].split(':')[1].strip()

    @property
    def get_content_length(self)->str:
        return self.__header_Assembled[3].split(':')[1].strip()

    @property
    def get_user_agent(self)->str:
        return self.__header_Assembled[4].split(':')[1].strip()

    @property
    def get_content_type(self)->str:
        return self.__header_Assembled[6].split(':')[1].strip()

    @property
    def get_body(self)->str:
        if self.get_method=="POST" or self.get_method=="UPDATE":
            return self.__header_Assembled[-1]
        return None