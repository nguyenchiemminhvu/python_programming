from typing import List
from dataclasses import dataclass, field # python3.7+

@dataclass
class Person:
    name: str = field(default="Unknown")
    age: int = field(default=0)
    jobs: List[str] = field(default_factory=list)

if __name__ == "__main__":
    person = Person(name="Alice", age=30, jobs=["Engineer", "Writer"])
    print(person)
    
    # Example of using default values
    default_person = Person()
    print(default_person)
    
    # Example of modifying the jobs list
    person.jobs.append("Artist")
    print(person.jobs)