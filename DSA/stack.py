# we can also do it using deque from collections as 
# from collections import deque  
# class Queue:
#     def __init__(self):
#         self.stack = deque()

class Stack:
    def __init__ (self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "stack is empty"
        
    def pop(self):
        if not self.is_empty():
            self.stack.pop()
        else:
            return "Cannot pop in an empty stack"
        
    def display(self):
        return self.stack
            
                

my_stack = Stack()
print(my_stack.is_empty())

my_stack.push(3)
my_stack.push(4)
my_stack.push(5)
print(my_stack.display())

print(my_stack.peek())

my_stack.pop()
print(my_stack.display())

