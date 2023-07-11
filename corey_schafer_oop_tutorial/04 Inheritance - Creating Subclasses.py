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

    @classmethod
    def from_string(cls, emp_str: str) -> "Employee":
        first, last, pay = emp_str.split("-")
        return cls(first, last, "company", int(pay))
    
    @staticmethod
    def is_workday(day) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    pass

dev_1 = Developer("Corey", "Schafer", "company", 50000)
dev_2 = Developer("Test", "Employee", "company", 60000)

print(dev_1.email)
print(dev_2.email)

print(help(Developer))
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
    
    @staticmethod
    def is_workday(day) -> bool:
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

class Developer(Employee):
    raise_amount = 1.10

dev_1 = Developer("Corey", "Schafer", "company", 50000)
dev_2 = Developer("Test", "Employee", "company", 60000)

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)
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

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first: str, last: str, company: str, pay: int, prog_lang: str) -> None:
        super().__init__(first, last, company, pay)
        # Employee.__init__(self, first, last, company, pay)
        self.prog_lang = prog_lang

dev_1 = Developer("Corey", "Schafer", "company", 50000, "Python")
dev_2 = Developer("Test", "Employee", "company", 60000, "Java")

print(dev_1.email)
print(dev_1.prog_lang)
"""

""" Part 4
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

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first: str, last: str, company: str, pay: int, prog_lang: str) -> None:
        super().__init__(first, last, company, pay)
        # Employee.__init__(self, first, last, company, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first: str, last: str, company: str, pay: int, employees: list|None) -> None:
        super().__init__(first, last, company, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp: Employee) -> None:
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp: Employee) -> None:
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self) -> None:
        for emp in self.employees:
            print(f"--> {emp.fullname()}")
        
dev_1 = Developer("Corey", "Schafer", "company", 50000, "Python")
dev_2 = Developer("Test", "Employee", "company", 60000, "Java")

mgr_1 = Manager("Sue", "Smith", "company", 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.print_emps()

mgr_1.remove_emp(dev_1)
mgr_1.print_emps()
"""

""" Part 5
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

class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first: str, last: str, company: str, pay: int, prog_lang: str) -> None:
        super().__init__(first, last, company, pay)
        # Employee.__init__(self, first, last, company, pay)
        self.prog_lang = prog_lang

class Manager(Employee):

    def __init__(self, first: str, last: str, company: str, pay: int, employees: list|None) -> None:
        super().__init__(first, last, company, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp: Employee) -> None:
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp: Employee) -> None:
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self) -> None:
        for emp in self.employees:
            print(f"--> {emp.fullname()}")
        
dev_1 = Developer("Corey", "Schafer", "company", 50000, "Python")
dev_2 = Developer("Test", "Employee", "company", 60000, "Java")

mgr_1 = Manager("Sue", "Smith", "company", 90000, [dev_1])

print(isinstance(mgr_1, Manager))
print(isinstance(mgr_1, Employee))
print(isinstance(mgr_1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
"""