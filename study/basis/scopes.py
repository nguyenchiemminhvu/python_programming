var = 10

class ScopeTest:
    def __init__(self):
        self.var = 0
    
    def test_local(self):
        var = 5
        print("Local var:", var)

    def test_global(self):
        global var
        print("Global var:", var)

    def test_class(self):
        print("Class var:", self.var)

s = ScopeTest()
s.test_local()
s.test_global()
s.test_class()