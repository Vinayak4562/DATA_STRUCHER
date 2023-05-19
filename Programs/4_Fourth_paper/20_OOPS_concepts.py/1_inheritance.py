#INHERITANCE 
# by inheriting the parent class in child class
print("SINGLE LEVEL INHERITANCE ") 
class parent:
    def pdisplay(self):
        print("Hey i am from parent class..!")

class child(parent):
    def cdisplay(self):
        print("Hey i am from child class..!")

obj1 = child()
obj1.cdisplay()
obj1.pdisplay()

print("=============================================================")
# Multileval LEVEL INHERITANCE
# here we are inheriting a class that has already inherited some other class
print("Multileval LEVEL INHERITANCE ")
class GrandParent:
    def gdisplay(self):
        print("Hey i am from GrandParent Class...!") 

class parent(GrandParent):
    def pdisplay(self):
        print("Hey i am from parent class..!")

class child(parent):
    def cdisplay(self):
        print("Hey i am from child class..!")

obj2=child()
obj2.cdisplay()
obj2.pdisplay()
obj2.gdisplay()

print("===========================================================")
# Multiple LEVEL INHERITANCE
print("Multiple LEVEL INHERITANCE ")
class father:
    def fdisplay(self):
        print("Hey i am from father Class...!") 

class mother:
    def mdisplay(self):
        print("Hey i am from mother class..!")

class child(father,mother):
    def cdisplay(self):
        print("Hey i am from child class i am inherithin from father as well as morher classes..!")

obj3=child()
obj3.cdisplay()
obj3.fdisplay()
obj3.mdisplay()

print("===========================================================")
# Hirarchial INHERITANCE
print("Hirarchial INHERITANCE ")
class parent:
    def pdisplay(self):
        print("Hey i am from parent Class...!") 

class child1(parent):
    def c1display(self):
        print("Hey i am from child1 class..!")

class child2(parent):
    def c2display(self):
        print("Hey i am from child2 class..!")

obj4=child1()
obj5=child2()

obj4.c1display()
obj5.c2display()

print("===========================================================")

class Vehicle:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    
    def display_info(self):
        print(f"{self.name} is {self.color}")

class Car(Vehicle):
    def __init__(self, name, color, model):
        super().__init__(name, color)
        self.model = model

    def display_info(self):
        print(f"{self.name} is {self.color} and is a {self.model} car")
        
car = Car("BMW", "red", "sedan")
car.display_info()
