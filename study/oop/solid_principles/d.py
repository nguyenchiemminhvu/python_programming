# Dependency inversion principle
# A class should depend on abstractions, not on concretions, meaning that high-level modules should not depend on low-level modules, but both should depend on abstractions.

# bad example

class OracleDatabase:
    def connect(self):
        print("Connecting to Oracle Database")
    
    def execute_query(self, query):
        print(f"Executing query on Oracle Database: {query}")

class UserService:
    def __init__(self):
        self.database = OracleDatabase()  # High-level module depends on low-level module
    
    def get_user(self, user_id):
        self.database.connect()
        self.database.execute_query(f"SELECT * FROM users WHERE id = {user_id}")

# good practice

from abc import ABC, abstractmethod

class i_database(ABC):
    @abstractmethod
    def connect(self):
        raise NotImplementedError("Subclasses must implement this method")
    
    @abstractmethod
    def execute_query(self, query):
        raise NotImplementedError("Subclasses must implement this method")

class my_sql_database(i_database):
    def connect(self):
        print("Connecting to MySQL Database")
    
    def execute_query(self, query):
        print(f"Executing query on MySQL Database: {query}")

class oracle_database(i_database):
    def connect(self):
        print("Connecting to Oracle Database")
    
    def execute_query(self, query):
        print(f"Executing query on Oracle Database: {query}")

class user_service:
    def __init__(self, database: i_database):
        self.database = database  # High-level module depends on abstraction

    def get_user(self, user_id):
        self.database.connect()
        self.database.execute_query(f"SELECT * FROM users WHERE id = {user_id}")