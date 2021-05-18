class Node:
    def __init__(self, key):
        self.left=None
        self.right=None
        self.key=key

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key)
        inorder(root.right)

def minNode(root):
    if root.left:
        return minNode(root.left)
    return root

def deleteNode(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = deleteNode(root.left, key)

    elif key > root.key:
        root.right = deleteNode(root.right, key)

    else:

        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = minNode(root.right)

        root.key = temp.key

        root.right = deleteNode(root.right, temp.key)

    return root

def insert(node, key):

    # If the tree is empty, return a new node
    if node is None:
        return Node(key)

    # Otherwise recur down the tree
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)

    # return the (unchanged) node pointer
    return node

# Driver code
""" Let us create following BST
            50
        /    \
        30   70
        / \ / \
    20 40 60 80 """

root = None
root = insert(root, 50)
root = insert(root, 30)
root = insert(root, 20)
root = insert(root, 40)
root = insert(root, 70)
root = insert(root, 60)
root = insert(root, 80)

print "Inorder traversal of the given tree"
inorder(root)

print "\nDelete 20"
root = deleteNode(root, 20)
print "Inorder traversal of the modified tree"
inorder(root)

print "\nDelete 30"
root = deleteNode(root, 30)
print "Inorder traversal of the modified tree"
inorder(root)

print "\nDelete 50"
root = deleteNode(root, 50)
print "Inorder traversal of the modified tree"
inorder(root)

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)
