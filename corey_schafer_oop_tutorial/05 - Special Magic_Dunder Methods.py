""" Part 1
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first: str, last: str, company: str, pay: int) -> None:
        self.first = first 
        self.last = last 
        self.company = company 
        self.pay = pay 
        self.email = f"{first}.{last}@{company}.com"

        Employee.num_of_emps += 1
    
    def fullname(self) -> str:
        return f"{self.first} {self.last}"
    
    def apply_raise(self) -> int:
        self.pay = int(self.pay * self.raise_amount)
        return self.pay
    
    def __repr__(self) -> str:
        return f"Employee('{self.first}', '{self.last}', '{self.company}', {self.pay})"

    def __str__(self) -> str:
        return f"{self.fullname()} - {self.email}"

emp_1 = Employee("Corey", "Schafer", "company", 50000)
emp_2 = Employee("Test", "User", "company", 60000)

print(emp_1)
print(emp_2)

print(repr(emp_1))
print(str(emp_1))

print(emp_1.__repr__())
print(emp_1.__str__())
"""

""" Part 2
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first: str, last: str, company: str, pay: int) -> None:
        self.first = first 
        self.last = last 
        self.company = company 
        self.pay = pay 
        self.email = f"{first}.{last}@{company}.com"

        Employee.num_of_emps += 1
    
    def fullname(self) -> str:
        return f"{self.first} {self.last}"
    
    def apply_raise(self) -> int:
        self.pay = int(self.pay * self.raise_amount)
        return self.pay
    
    def __repr__(self) -> str:
        return f"Employee('{self.first}', '{self.last}', '{self.company}', {self.pay})"

    def __str__(self) -> str:
        return f"{self.fullname()} - {self.email}"
    
    def __add__(self, other) -> int:
        return self.pay + other.pay

emp_1 = Employee("Corey", "Schafer", "company", 50000)
emp_2 = Employee("Test", "User", "company", 60000)

print(emp_1 + emp_2)
"""

""" Part 3
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first: str, last: str, company: str, pay: int) -> None:
        self.first = first 
        self.last = last 
        self.company = company 
        self.pay = pay 
        self.email = f"{first}.{last}@{company}.com"

        Employee.num_of_emps += 1
    
    def fullname(self) -> str:
        return f"{self.first} {self.last}"
    
    def apply_raise(self) -> int:
        self.pay = int(self.pay * self.raise_amount)
        return self.pay
    
    def __repr__(self) -> str:
        return f"Employee('{self.first}', '{self.last}', '{self.company}', {self.pay})"

    def __str__(self) -> str:
        return f"{self.fullname()} - {self.email}"
    
    def __add__(self, other) -> int:
        return self.pay + other.pay
    
    def __len__(self) -> int:
        return len(self.fullname())

emp_1 = Employee("Corey", "Schafer", "company", 50000)
emp_2 = Employee("Test", "User", "company", 60000)

print(len(emp_1))
"""