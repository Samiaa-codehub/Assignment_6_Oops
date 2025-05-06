## Aggregation ###
##Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self,name, position):
      self.name = name
      self.position = position
      
    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Position: {self.position}")

class Department:
  def __init__(self,name,department_name):
    self.name = name
    self.department_name = department_name

  def department_info(self):
    print(f"Name: {self.name}")
    print(f"Department Name: {self.department_name}")

emp1 = Employee("Samia","Developer")
dep1 = Department("Ali","IT")

emp1.display_info()
dep1.department_info()
