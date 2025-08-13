# Open/close principle
# # A class should be open for extension but closed for modification, meaning that you should be able to add new functionality without changing existing code.

# bad example
class Employee:
    def __init__(self):
        self.salary = 0

class Tester(Employee):
    def test(self):
        print("Running tests...")

class Developer(Employee):
    def develop(self):
        print("Developing features...")

class Company:
    def __init__(self, budget):
        self.budget = budget
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
            print(f"Added {employee.__class__.__name__} with salary {employee.salary}.")

    def perform_tasks(self):
        for employee in self.employees:
            if isinstance(employee, Tester):
                employee.test()
                employee.salary += 1000
                self.budget -= 1000
            elif isinstance(employee, Developer):
                employee.develop()
                employee.salary += 2000
                self.budget -= 2000

        for employee in self.employees:
            print(f"{employee.__class__.__name__} salary: {employee.salary}")

com = Company(10000000)
com.add_employee(Tester())
com.add_employee(Developer())
com.perform_tasks()
com.perform_tasks()
com.perform_tasks()

# good practice
from typing import List, Dict
from abc import ABC, abstractmethod

class Worker(ABC):
    def __init__(self):
        self.salary = 0

    @abstractmethod
    def perform_task(self):
        pass

class QA(Worker):
    def perform_task(self):
        print("Running tests...")
        super().perform_task()

class Dev(Worker):
    def perform_task(self):
        print("Developing features...")
        super().perform_task()

class Project:
    def __init__(self, name):
        self.name = name

class Organization:
    def __init__(self, budget):
        self.budget = budget
        self.workers = []
        self.projects : Dict[str, List[Worker]] = {}

    def add_worker(self, worker, salary):
        worker.salary = salary
        self.workers.append(worker)

    def add_project(self, project):
        self.projects[project.name] = []

    def assign_worker_to_project(self, worker, project):
        if worker in self.workers and project.name in self.projects:
            print(f"Assigning {worker.__class__.__name__} to project {project.name}.")
            if (not worker in self.projects[project.name]):
                print(f"{worker.__class__.__name__} assigned to project {project.name}.")
                self.projects[project.name].append(worker)
            else:
                print(f"{worker.__class__.__name__} is already assigned to project {project.name}.")

    def perform_tasks(self):
        for project_name, workers in self.projects.items():
            print(f"Performing tasks for project {project_name}:")
            for worker in workers:
                worker.perform_task()
                self.budget -= worker.salary
            print(f"Remaining budget: {self.budget}")
        self.projects.clear()

org = Organization(10000000)
qa1 = QA()
dev1 = Dev()
org.add_worker(qa1, 1000)
org.add_worker(dev1, 2000)

pro1 = Project("Project A")
org.add_project(pro1)

org.assign_worker_to_project(qa1, pro1)
org.assign_worker_to_project(dev1, pro1)
org.perform_tasks()