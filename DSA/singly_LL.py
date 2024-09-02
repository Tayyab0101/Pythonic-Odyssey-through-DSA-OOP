class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return

        itr = self.head
        while itr.next is not None:
            itr = itr.next
        itr.next = new_node
    
    def __str__(self):
        if self.head is None:
            return "LinkedList is empty"
        
        itr = self.head
        result = ""
        while itr:
            result += str(itr.data) + " --> "
            itr = itr.next
        result += "None"
        return result
        
ll = LinkedList()
ll.insert(4)
ll.insert(5)
ll.insert(6)

print(ll)