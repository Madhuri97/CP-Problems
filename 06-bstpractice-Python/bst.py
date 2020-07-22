class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        # Your code goes here
        if self.root.value == new_val:
            return False
        elif new_val < self.root.value:
            if self.root.left:
                return self.root.left.insert(new_val)
            else:
                self.root.left = Node(new_val)
                return True
        else: 
            if self.root.right:
                return self.root.right.insert(new_val)
            else:
                self.root.right = Node(new_val)
                return True

    def printSelf(self):
        # Your code goes here
        pass
        
    def search(self, find_val):
        # Your code goes here
        pass

