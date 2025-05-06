#Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.italicized text
class  Car:
    brand="Toyota"
    def start(self):
        return(f"The {self.brand} car is starting.")
my_car = Car()
print(my_car.brand) # Accessing the public variable
print(my_car.start()) # Accessing the public method


