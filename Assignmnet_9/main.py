## Abstract Classes and Methods
## Use the abc module to create an abstract class Shape with an abstract method area(). Inherit a class Rectangle that implements area().
from abc import ABC,abstractmethod

class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class Rectangle(shape):
    def __init__(self,width,height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
rec = Rectangle(5,10)
print(f"Area of Rectangle:{rec.area()}")