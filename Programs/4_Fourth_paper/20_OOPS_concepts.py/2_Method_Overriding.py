'''Method overriding is a mechanism where a subclass provides its 
implementation of a method that is already provided by its parent class.'''
class Animal:
    def speak(self):
        print("The animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("The dog barks")

dog = Dog()
dog.speak()
