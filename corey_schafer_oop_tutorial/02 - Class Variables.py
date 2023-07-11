""" Part 1
class Employee:

    def __init__(self, first: str, last: str, company: str, pay: int) -> None:
        self.first = first 
        self.last = last 
        self.company = company 
        self.pay = pay 
        self.email = f"{first}.{last}@{company}.com"
    
    def fullname(self) -> str:
        return f"{self.first} {self.last}"
    
    def apply_raise(self) -> int:
        self.pay = int(self.pay * 1.04)
        return self.pay
    
emp_1 = Employee("Corey", "Schafer", "company", 50000)
emp_2 = Employee("Test", "User", "company", 60000)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)
"""


""" Part 2
class Employee:

    raise_amount = 1.04

    def __init__(self, first: str, last: str, company: str, pay: int) -> None:
        self.first = first 
        self.last = last 
        self.company = company 
        self.pay = pay 
        self.email = f"{first}.{last}@{company}.com"
    
    def fullname(self) -> str:
        return f"{self.first} {self.last}"
    
    def apply_raise(self) -> int:
        self.pay = int(self.pay * self.raise_amount)
        return self.pay
    
emp_1 = Employee("Corey", "Schafer", "company", 50000)
emp_2 = Employee("Test", "User", "company", 60000)

emp_1.raise_amount = 1.05

print(emp_1.__dict__)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
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

print(Employee.num_of_emps)

emp_1 = Employee("Corey", "Schafer", "company", 50000)
emp_2 = Employee("Test", "User", "company", 60000)

print(Employee.num_of_emps)
"""