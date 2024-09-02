# Python is a duck typing languauge that means data type of a variable can change as long as the syntax is compatible (means methods are defined)
class Dog:
    def swim(self):
        print("I'm a dog and I can swim")
    
    def display(self):
        print("Display from Dog class")
        
    def bark(self):
        print("I am a dog and I bark")
        
class Owl:
    def swim(self):
        print("I am an owl and I don't swim")
        
    def bark(self):
        print("I am an owl and I don't bark")
        
def display(obj): #obj can be changed or of any type but what matter is the methods it have....
    obj.swim()
    obj.bark()
  
dog1 = Dog() #Instance of Dog
owl1 = Owl() # Instance of owl
dog1.display()
display(owl1)

