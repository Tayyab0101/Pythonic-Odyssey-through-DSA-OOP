from collections import deque

class PriorityQueue:
    def __init__(self):
        self.queue = deque()
        
    def is_empty(self):
        return len(self.queue) == 0
    
    def enqueue(self, item):
        self.queue.append(item)  # Append to the end of the queue
        
    def dequeue(self):
        if not self.is_empty():
            min_item = max(self.queue)  # Find the item with the highest priority
            self.queue.remove(min_item)  # Remove that item from the queue
            return min_item  # Return the removed item
        else:
            return "It's an empty queue"
        
    def front(self):
        if not self.is_empty():
            return self.queue[0]  # Get the front item
        else:
            return "It's an empty queue"
    
    def rear(self):
        if not self.is_empty():
            return self.queue[-1]  # Get the rear item
        else:
            return "It's an empty queue"
    
    def display(self):
        return list(self.queue)  # Convert deque to list for display

# Example usage
new_queue = PriorityQueue()
print(new_queue.is_empty())  # Should print True

new_queue.enqueue(11)
new_queue.enqueue(23)
new_queue.enqueue(13)
print(new_queue.display()) 

print(new_queue.front())  

print(new_queue.dequeue())  
print(new_queue.display())  

print(new_queue.rear()) 
