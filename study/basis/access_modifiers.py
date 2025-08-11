# demonstrate access modifiers of class in Python

class Mapping:
    def __init__(self):
        self.public = "public"  # public attribute
        self._protected = "protected"  # protected attribute
        self.__private = "private"  # private attribute

    def get_private(self):
        return self.__private  # method to access private attribute

    def _get_protected(self):
        return self._protected  # method to access protected attribute

class SubMapping(Mapping):
    def __init__(self):
        super().__init__()

    def access_protected(self):
        return self._protected  # can access protected attribute

    def access_private(self):
        return self.get_private()  # can access private attribute through method

if __name__ == "__main__":
    mapping = Mapping()
    print("Public:", mapping.public)  # accessible
    print("Protected:", mapping._protected)  # accessible but should be treated as protected
    print("Private (via method):", mapping.get_private())  # accessible through method

    sub_mapping = SubMapping()
    print("Accessing protected from subclass:", sub_mapping.access_protected())  # accessible
    print("Accessing private from subclass:", sub_mapping.access_private())  # accessible through method