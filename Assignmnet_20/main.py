# Creating a custom exception ..
#Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.
class InvalidAgeError(Exception):
    def __init__(self,message="Age must be 18 or older"):
        self.message = message
        super().__init__(self.message)
def check_age(age):
        if age < 18:
            raise InvalidAgeError(f"Invalid age: {age}. Age must be 18 or older.")
        else:
            print(f"Valid age: {age}.")
try:
    age = int(input("Enter your age: "))
    check_age(age)
except InvalidAgeError as e:
    print(e)
except ValueError:
    print("Invalid input. Please enter a number.")
