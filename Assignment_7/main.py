#Create a class Employee with:
#a public variable name,

#a protected variable _salary, and

#a private variable __ssn.

#Try accessing all three variables from an object of the class and document what happens.
class Employee:
    name = "Ali"

    _salary = 5000

    __ssn = "123-45-6789"
# Creating an object of Employee class
emp = Employee()
print("Name:",emp.name)
print("Salary:",emp._salary)
try:
    print("SSN:",emp.__ssn)
except AttributeError as e:
    print("Error:",e)
print("SSN (via name manging):", emp._Employee__ssn)