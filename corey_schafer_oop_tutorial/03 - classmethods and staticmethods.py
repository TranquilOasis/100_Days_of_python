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
    
    @classmethod
    def set_raise_amt(cls, amount: float) -> None:
        cls.raise_amount = amount

emp_1 = Employee("Corey", "Schafer", "company", 50000)
emp_2 = Employee("Test", "User", "company", 60000)

Employee.set_raise_amt(1.05)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
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
    
    @classmethod
    def set_raise_amt(cls, amount: float) -> None:
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str) -> "Employee":
        first, last, pay = emp_str.split("-")
        return cls(first, last, "company", int(pay))
    
emp_str_1 = "John-Doe-70000"
emp_str_2 = "Steve-Smith-30000"
emp_str_3 = "Jane-Doe-90000"

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)
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
    
    @classmethod
    def set_raise_amt(cls, amount: float) -> None:
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str) -> "Employee":
        first, last, pay = emp_str.split("-")
        return cls(first, last, "company", int(pay))
    
    @staticmethod
    def is_workday(day) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee("Corey", "Schafer", "company", 50000)
emp_2 = Employee("Test", "User", "company", 60000)

import datetime
my_date = datetime.date(2021, 7, 11)

print(Employee.is_workday(my_date))
"""