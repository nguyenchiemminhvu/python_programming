from abc import ABC, abstractmethod

class interface(ABC):
    @abstractmethod
    def operation(self):
        pass

class real_service(interface):
    def operation(self):
        return "Real service operation executed."

class proxy_service(interface):
    def __init__(self, p_service : interface):
        self._p_service = p_service
    
    def restrict_check(self):
        print("Restriction check passed.")
        return True
    
    def record_access(self):
        print("Access recorded.")
    
    def operation(self):
        self.record_access()
        if self.restrict_check():
            return self._p_service.operation()
        else:
            return "Access denied."

# Client code
if __name__ == "__main__":
    real = real_service()
    proxy = proxy_service(real)
    
    print(proxy.operation())