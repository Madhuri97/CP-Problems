"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        
    def append(self, new_element):
        # Your code goes here
        node = Element(new_element)
        if self.head:
            self.head.next = node
            self.head = node
            
    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        if self.head is None:
            return None
        node = self.head
        while node is not None:
            if node.value == position:
                return position.value
            node = node.next
        return None
    
    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        if position is None:
            pass
        node = Element(new_element)
        node.next = position.next
        position.next = node
    
    def delete(self, value):
        """Delete the first node with a given value."""
        node = self.head
        if node is not None:
            if(node.value == value):
                self.head = node.next
                node = None
