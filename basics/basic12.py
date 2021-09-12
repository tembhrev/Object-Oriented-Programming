class Employee:
    "Common base class for all employees"
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def display(self):
        pass

    def displayEmployee(self):
        pass

emp1 = Employee("Sushma", 2000)

#Checking for existence of attribute name
if hasattr(emp1, 'age'):
    print("Instance 'emp1' has attribute 'age' ")
else:
    print("Instance 'emp1' has NO attribute 'age' ")

print("Value of attribute 'name' in instance 'emp1' is", getattr(emp1, 'name'))

#Setting new value for attribute name
setattr(emp1, 'name', 'Arihant')

#Check with getattr name change
print("Value of attribute 'name' in instance 'emp1' after name change is", getattr(emp1, 'name'))

#deleting attribute name.
delattr(emp1, 'name')

#check withn hasattr
if hasattr(emp1, 'name'):
    print("Instance 'emp1' has attribute 'name'")
else:
    print("Instance 'emp1' has NO attribute 'name'")
    
