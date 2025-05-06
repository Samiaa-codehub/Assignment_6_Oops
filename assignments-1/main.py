### Using the self keyword ####
#Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.italicized text
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print(f"Name: {self.name} , Marks: {self.marks}")
s1=Student("Ali", 90)
s2=Student("Sara", 85)
s3=Student("Sana", 95)
s1.display()
s2.display()
s3.display()



