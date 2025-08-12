import weakref, gc

class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} created")
    
    def __del__(self):
        print(f"{self.name} deleted")

def demo_weak_ref():
    # Create an instance of MyClass
    obj = MyClass("MyObject")
    
    # Create a weak reference to the object
    weak_ref = weakref.ref(obj)
    
    # Access the object through the weak reference
    print(f"Weak reference points to: {weak_ref()}, ref counter: {weakref.getweakrefcount(obj)}")
    
    # Delete the original object
    del obj
    
    # Force garbage collection
    gc.collect()
    
    # Check if the weak reference is still valid
    print(f"Weak reference after deletion: {weak_ref()}")

def demo_weak_key():
    obj1, obj2 = MyClass("WeakKeyObject1"), MyClass("WeakKeyObject2")
    weak_key_dict = weakref.WeakKeyDictionary()
    weak_key_dict[obj1] = "Some value"
    weak_key_dict[obj2] = "Another value"
    print(f"WeakKeyDictionary contains: {weak_key_dict}")
    print(f"Value for obj1: {weak_key_dict.get(obj1)}")
    del obj1  # Remove one object
    gc.collect()  # Force garbage collection
    print(f"WeakKeyDictionary after deletion: {weak_key_dict}")
    # get values
    print(f"Value for obj2: {weak_key_dict.get(obj2)}")

if __name__ == "__main__":
    demo_weak_ref()
    demo_weak_key()