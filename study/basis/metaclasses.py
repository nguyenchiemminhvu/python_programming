from ncmv import default_logging
import logging

class SingletonMeta(type):
    """
    A metaclass for creating singleton classes.
    """
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class InterfaceEnforceMeta(type):
    """
    A metaclass that enforces the implementation of specified methods in subclasses.
    """
    def __new__(cls, name, bases, attrs):
        if "required_method" not in attrs:
            raise TypeError(f"Class {name} must implement 'required_method'")
        return super().__new__(cls, name, bases, attrs)
    
    def __instancecheck__(self, instance):
        required_methods = getattr(self, 'required_method', [])
        return all(callable(getattr(instance, method, None)) for method in required_methods)
    
    def __subclasscheck__(self, cls):
        required_methods = getattr(self, 'required_method', [])
        return all(callable(getattr(cls, method, None)) for method in required_methods)

class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        pass

class ExampleInterface(metaclass=InterfaceEnforceMeta):
    def required_method(self):
        pass

s1 = Singleton()
s2 = Singleton()
logging.info(f"Singleton instances are the same: {s1 is s2}")
logging.info(f"Singleton instance: {s1}")
logging.info(f"Singleton instance: {s2}")

e1 = ExampleInterface()