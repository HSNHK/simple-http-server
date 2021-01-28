
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
