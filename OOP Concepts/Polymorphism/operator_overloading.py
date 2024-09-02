class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __add__(self, other):
        return f"add operator is being defined here.\nThe data of Person instances is as: {self.name} is {self.age} years old and {other.name} is {other.age} years old."
    
    def __gt__(self, other):
        return self.age > other.age
        
p1 = Person("Tayyab", 24)
p2 = Person("Ali", 26)

c = p1 + p2
print(c)

if p1 > p2:
    print(f"{p1.name} is older than {p2.name}")
else:
    print(f"{p2.name} is older than {p1.name}")
