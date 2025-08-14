# Interface segregation principle
# A class should not be forced to implement interfaces it does not use, meaning that clients should not be forced to depend on methods they do not use.

# bad example

from abc import ABC, abstractmethod

class ILocationParser(ABC):
    @abstractmethod
    def parse_ubx(self, buffer):
        raise NotImplementedError("This method is not implemented")
    
    @abstractmethod
    def parse_nmea(self, buffer):
        raise NotImplementedError("This method is not implemented")

class UBXParser(ILocationParser):
    def parse_ubx(self, buffer):
        # UBX parsing logic
        pass
    
    def parse_nmea(self, buffer):
        # This method is not used, but must be implemented
        raise NotImplementedError("This method is not implemented")

class NMEAParser(ILocationParser):
    def parse_nmea(self, buffer):
        # NMEA parsing logic
        pass
    
    def parse_ubx(self, buffer):
        # This method is not used, but must be implemented
        raise NotImplementedError("This method is not implemented")

# good practice

class Iubx(ABC):
    @abstractmethod
    def parse_ubx(self, buffer):
        raise NotImplementedError("This method is not implemented")

class Inmea(ABC):
    @abstractmethod
    def parse_nmea(self, buffer):
        raise NotImplementedError("This method is not implemented")

class UBXParser(Iubx):
    def parse_ubx(self, buffer):
        # UBX parsing logic
        pass

class NMEAParser(Inmea):
    def parse_nmea(self, buffer):
        # NMEA parsing logic
        pass