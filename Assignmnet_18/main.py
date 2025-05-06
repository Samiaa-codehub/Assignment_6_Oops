## property decorator Setters and Deleters
##Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

class Product:
  def __init__(self,price):
    self._price = price
  @property
  def price(self):
    return self._price
  @price.setter
  def price(self,value):
    if value < 0:
      print("Price can not be negative!")
    else:
        self.value = value

  @price.deleter
  def price(self):
    print("Deleling price...")
  

p = Product(100)
print(p.price)

p._price = 150
print(p.price)

p.price = -20
del p.price