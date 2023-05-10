'''
Day 69 coding Statement :Triangle Classification
Suppose, we have a class A which is the base class and we have a class B which is derived from class A and we have a class C which is derived from class B, we can access the functions of both class A and class B by creating an object for class C.
Hence, this mechanism is called multi-level inheritance. (B inherits A and C inherits B.)
Create a class called Equilateral which inherits from Isosceles and should have a function such that the output is as given below.

Sample Output
I am an equilateral triangle
I am an isosceles triangle I am a triangle

'''
class Isosceles:
  def display1(self):
    print("I am an isosceles triangle")

class Equilateral(Isosceles):
  def display2(self):
    print("I am  an equilateral triangle")

class C(Equilateral):
  def display3(self):
    print("I am a triangle")

obj = C()
obj.display2()
obj.display1()
obj.display3()