class Queue:
    def __init__(self):
        self.queue = []
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, index, item):  # in case of append whole scenarios would have to be chnaged
        self.queue.insert(index, item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(-1)
        else:
            return "Its an empty queue"
    
    def front(self):
        if not self.is_empty():
            return self.queue[-1]
        else:
            return "its an empty queue"
        
    def rear(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            return "Its an empty queue"
        
    def display(self):
        return list(self.queue)
    
new_queue = Queue()
print(new_queue.is_empty())

new_queue.enqueue(0, 5)
new_queue.enqueue(0, 6)
new_queue.enqueue(0, 7)
new_queue.enqueue(0, 8)
print(new_queue.display())

new_queue.dequeue()
print(new_queue.display())

print(new_queue.front())
print(new_queue.rear())