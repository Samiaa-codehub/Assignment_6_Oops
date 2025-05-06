 # Define the class decorator
def add_greeting(cls):
    # Define the greet method
    def greet(self):
        return "Hello from Decorator!"
    
    # Add the method to the class
    setattr(cls, 'greet', greet)
    return cls

# Apply the decorator to the Person class
@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

    def intoduce(self):  # Note: Typo in 'intoduce'—should be 'introduce' ideally
        return f"Hello, my name is {self.name}."

# Create an instance and test the methods
person = Person("Samia")
print(person.intoduce())  # Output: Hello, my name is Samia.
print(person.greet())     # Output: Hello from Decorator!
