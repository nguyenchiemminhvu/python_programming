from abc import ABC, abstractmethod

class request:
    def __init__(self):
        pass

class handler(ABC):
    @abstractmethod
    def handle_request(self, req):
        raise NotImplementedError("Subclasses should implement this method")
    
    @abstractmethod
    def set_next(self, obj : "handler"):
        raise NotImplementedError("Subclasses should implement this method")

class base_handler(handler):
    def __init__(self):
        self.__next_handler__ = None
    
    def handle_request(self, req):
        if (self.__next_handler__ is not None):
            self.__next_handler__.handle_request(req)
    
    def set_next(self, obj):
        if not isinstance(obj, handler):
            raise TypeError("Expected an instance of handler")
        self.__next_handler__ = obj
        return obj

class authentication_handler(base_handler):
    def __init__(self):
        super().__init__()
    
    def handle_request(self, req):
        if not self.__authenticate(req):
            print("Authentication failed")
            req.auth = False
            return
        req.auth = True
        super().handle_request(req)
    
    def __authenticate(self, req):
        if (req.username == "admin" and req.password == "password"):
            return True
        return False

class cache_handler(base_handler):
    def __init__(self):
        super().__init__()
        self.__cache__ = set()

    def handle_request(self, req):
        if req.command and req.command in self.__cache__:
            print("Cache hit")
        else:
            print("Cache miss")
            self.__cache__.add(req.command)

        super().handle_request(req)

if __name__ == "__main__":
    req = request()
    req.username = "admin"
    req.password = "password"
    req.command = "get_data"
    
    head = base_handler()
    head.set_next(authentication_handler()) \
        .set_next(cache_handler())

    head.handle_request(req)
    head.handle_request(req)
    
    req.username = "user"
    head.handle_request(req)