class Node:
	def __init__(self,key):
		self.left= None
		self.right=None
		self.data=key

def minimum(node):
	if node.left:
		return minimum(node.left)
	return node.data

def treeSuccessor(node):
	if node.right:
		return minimum(node.right)
	y=node.parent
	while y and node == y.right:
		node = y
		y = node.parent
	return y

def insert( node, data):

    # 1) If tree is empty
    # then return a new singly node
    if node is None:
        return Node(data)
    else:
        
        # 2) Otherwise, recur down the tree
        if data <= node.data:
            temp = insert(node.left, data)
            node.left = temp
            temp.parent = node
        else:
            temp = insert(node.right, data)
            node.right = temp
            temp.parent = node
        
        # return the unchanged node pointer
        return node

# Driver progam to test above function
# Driver progam to test above function
if __name__ == "__main__":
    root = None

# Creating the tree given in the above diagram
root = insert(root, 20)
root = insert(root, 8);
root = insert(root, 22);
root = insert(root, 4);
root = insert(root, 12);
root = insert(root, 10);
root = insert(root, 144);
root = insert(root, 19);
temp = root.left.right

succ = treeSuccessor(temp)
print("Given:",temp.data)
print("Inorder Successor:" ,succ)
