# Python OOP Tutorial 1: Classes and Instances
# https://www.youtube.com/watch?v=ZDa-Z5JzLYM

""" Part 1
class Employee:
    pass

emp_1 = Employee()
emp_2 = Employee()

emp_1.first = "Corey" # type: ignore
emp_1.last = "Schafer" # type: ignore
emp_1.email = f"{emp_1}.{emp_2}@company.com" # type: ignore
emp_1.pay = 50000 # type: ignore


emp_2.first = "Test" # type: ignore
emp_2.last = "User" # type: ignore
emp_2.email = f"{emp_1}.{emp_2}@company.com" # type: ignore
emp_2.pay = 60000 # type: ignore

print(emp_1.email) # type: ignore
print(emp_2.email) # type: ignore
"""

""" Part 2
class Employee:

    def __init__(self, first: str, last: str, company: str, pay: int) -> None:
        self.first = first 
        self.last = last 
        self.company = company 
        self.pay = pay 
        self.email = f"{first}.{last}@{company}.com"

emp_1 = Employee("Corey", "Schafer", "company", 50000)
emp_2 = Employee("Test", "User", "company", 60000)

print(emp_1.email)
print(emp_2.email)
"""


""" Part 3
class Employee:

    def __init__(self, first: str, last: str, company: str, pay: int) -> None:
        self.first = first 
        self.last = last 
        self.company = company 
        self.pay = pay 
        self.email = f"{first}.{last}@{company}.com"
    
    def fullname(self) -> str:
        return f"{self.first} {self.last}"

emp_1 = Employee("Corey", "Schafer", "company", 50000)
emp_2 = Employee("Test", "User", "company", 60000)

print(emp_1.fullname())
print(emp_2.fullname())
"""

# Part 4
class Employee:

    def __init__(self, first: str, last: str, company: str, pay: int) -> None:
        self.first = first 
        self.last = last 
        self.company = company 
        self.pay = pay 
        self.email = f"{first}.{last}@{company}.com"
    
    def fullname(self) -> str:
        return f"{self.first} {self.last}"
    
emp_1 = Employee("Corey", "Schafer", "company", 50000)
emp_2 = Employee("Test", "User", "company", 60000)

print(emp_1.fullname())
print(Employee.fullname(emp_1))