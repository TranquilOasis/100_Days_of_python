""" Part 1
class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first: str, last: str) -> None:
        self.first = first 
        self.last = last 

        Employee.num_of_emps += 1
    
    @property
    def email(self) -> str:
        return f"{self.first}.{self.last}@email"

    @property
    def fullname(self) -> str:
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name: str) -> None:
        first, last = name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self) -> None:
        print("Delete Name!")
        self.first = None
        self.last = None

emp_1 = Employee("John", "Smith")

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

emp_1.first = "Jim"
emp_1.fullname = "Corey Schafer"

print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname"""