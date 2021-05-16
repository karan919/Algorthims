class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def treeSearch(self, key):
        if key < self.data:
            if self.left is None:
                return str(key)+" Not Found"
            return self.left.treeSearch(key)
        elif key > self.data:
            if self.right is None:
                return str(key)+" Not Found"
            return self.right.treeSearch(key)
        else:
            return ("found at :" , self.data)

# Driver code
root = Node(1)
root.insert(2)
root.insert(3)
root.insert(4)

print(root.treeSearch(2))
