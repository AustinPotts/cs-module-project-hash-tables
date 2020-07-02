# Create Data Structure to represent Node
class Node:
    def __init__(self, value=None, next_node=None):
        # Has room for the value 
        self.value = value 
        # Has room for the next node 
        self.next_node = next_node

    def get_value(self):
        return self.value
    def get_next(self):
        return self.next_node
    def set_next(self,new_next):
        self.next_node = new_next

# It's really common to have an outer class that wraps up the linked list 
# Object that represents the Linked List 
class LinkedList:
    def __init__(self):
        # Indicating the linked list is empty 
        self.head = None 
        self.tail = None

    def add_to_tail(self,value):
        new_node = Node(value, None)

        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.set_next(new_node)
            self.tail = new_node
    
    def make_new_head(self,value):
        new_node = Node(value)
        previous_head = self.head
        self.head = new_node
        self.head.set_next(previous_head)

    def remove_head(self):
        if not self.head:
            return None
        if not self.head.get_next:
            head = self.head
            self.head = None
            self.tail = None 
            return head.get_value()
        
        value = self.head.get_value()
        self.head = self.head.get_next()
        return value

    def remove_tail(self):
        if not self.head:
            return None
        if self.head == self.tail:
            value = self.head.get_value()
            self.head = None 
            self.tail = None 
            return value
        current = self.head
        while current.get_next() != self.tail:
            current = current.get_next()
        value = self.tail.get_value()
        self.tail = current
        self.tail.set_next(None)
        return value
        
     # find the node value    
    def contains(self,value):
        if not self.head:
            return None

        current = self.head
        # Walk the linked list 
        while current:
            if current.get_value() == value:
                return current # Return the node 
            current = current.get_next()
        return None # Return None if fail

    def get_max(self):
        if not self.head:
            return None
        max_value = self.head.get_value()
        current = self.head.get_next()
        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.get_next()
        return max_value
    
    # From Beej Lecture 
    def delete(self, value):
        cur = self.head
            
        # Special case of deleting the head of the list
        if cur.value == value:
            self.head = self.head.next_node
            return cur
                
        # General case
        prev = cur
        cur = cur.next_node
            
        while cur is not None:
            if cur.value == value:  # Delete this one
                prev.next_node = cur.next_node   # Cuts out the old node
                return cur
            else:
                prev = prev.next_node
                cur = cur.next_node
        return None
