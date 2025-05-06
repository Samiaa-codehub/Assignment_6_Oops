#Create four classes:

#A with a method show(),

#B and C that inherit from A and override show(),

#D that inherits from both B and C.
#Create an object of D and call show() to observe MRO.




class A:
  def show(self):
    print("Show Class A")
class B(A):
  def show(self):
    print("Show Class B")
class C(A):
  def show(self):
    print("Show Class C")
class D(B,C):
  pass
d = D()
a = A()
a.show()
d.show()
print(D.mro())