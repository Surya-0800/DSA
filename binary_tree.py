'''In Binary Tree every node has atleast 2 children'''

class Node:
    def __init__(self,k):
        self.k = k
        self.left = None
        self.right = None

root_node = Node(10)
root_node.right = Node(30)
root_node.left = Node(20)
root_node.left.left = Node(25)


def inorder(root_node):
    if root_node != None:
        inorder(root_node.left)
        print(root_node.k)
        inorder(root_node.right)

def preorder(root):
    if root != None:
        print(root.k)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root != None:
        postorder(root.left)
        postorder(root.right)
        postorder(root.k)

# inorder(root_node)
preorder(root_node)