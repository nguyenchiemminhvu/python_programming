import time
from typing import List

class Person:
    def __init__(self, birth_year):
        self.birth_year = birth_year
    
    def get_age(self):
        cur_year = time.localtime().tm_year
        return cur_year - self.birth_year

class Student(Person):
    def __init__(self, birth_year, student_id):
        Person.__init__(self, birth_year)
        self.student_id = student_id
    
    def display_info(self):
        age = self.get_age()
        print(f"Student ID: {self.student_id}, Age: {age}")

class Teacher(Person):
    def __init__(self, birth_year, subject):
        Person.__init__(self, birth_year)
        self.subject = subject
    
    def display_info(self):
        age = self.get_age()
        print(f"Subject: {self.subject}, Age: {age}")

# multi inheritance
class StudentPartner(Student, Teacher):
    def __init__(self, birth_year, student_id, subject):
        Student.__init__(self, birth_year, student_id)
        Teacher.__init__(self, birth_year, subject)
    
    def display_info(self):
        age = self.get_age()
        print(f"Student ID: {self.student_id}, Subject: {self.subject}, Age: {age}")

def show_infor(persons:List[Person]):
    for person in persons:
        person.display_info()

s1 = Student(2000, "S12345")
t1 = Teacher(1980, "Mathematics")
p1 = StudentPartner(1995, "S54321", "Physics")

show_infor([s1, t1, p1])