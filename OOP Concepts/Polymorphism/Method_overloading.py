#Python doesnt support method over loading
# Method Overloading is same class, same multiple methods but with diffrent args
# This is compile-time polymorphism

class Calculator:
    def sum(self, a, b):
        return a + b
    
    # 1st - DEFAULT ARGUMENT. In case if we simply put c as arg 2nd print statement will fail and it will give Type Eroor. Because python doesn't support it and later method will be considered as master
    def sum(self, a, b, c=0):  
        return a + b + c
    
    #2nd - Using variable length arguments
    def sum(self, *args):
        total = 0
        for i in args:
            total += i
        return total
    
c1 = Calculator()
#printing first add method
print(c1.sum(1, 2))
#printing second add method
print(c1.sum(2, 5, 1)) #adding c is actually overriding previous c = 0
#printing tird add method
print(c1.sum(5, 6, 8, 9, 2))