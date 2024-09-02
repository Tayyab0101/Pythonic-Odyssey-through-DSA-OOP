# Method overriding should have atleast two classes and is inplemented in Inheritence only.
# This is run-time polymorphism

class Human:
    def eat(self):
        print("I can eat")
        
    def walk(self):
        print("I can walk")
        
class Male(Human):
    def eat(self):
        print("I need more calories than a lady")
        super().eat()
    
    def walk(self):
        print("I can walk and run faster tan a lady normally.")
    
m1 = Male()
m1.eat()