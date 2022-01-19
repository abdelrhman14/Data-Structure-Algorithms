class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
 
# 1- inorder [left ,root ,right]
def inorder(root):

    if root:
        inorder(root.left)
        print(root.val),
        inorder(root.right)
# 4 2 5 1 3
 
# 2- postorder [left, right, root]
def postorder(root):
 
    if root:
 
        postorder(root.left)
        postorder(root.right)
        print(root.val),
# 4 5 2 3 1
 
# 3- preorder [root, left, right]
def preorder(root):
 
    if root:
 
        print(root.val),
        preorder(root.left)
        preorder(root.right)

#  1 2 4 5 3
 
# Driver code
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("inorder traversal of binary tree is")
inorder(root)

print("\npreorder traversal of binary tree is")
preorder(root)
 
print("\npostorder traversal of binary tree is")
postorder(root)
