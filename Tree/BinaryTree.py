class Node:
    def __init__(self, key):
        self.left = None
        self.rigth = None
        self.val = key

root = Node(5)

root.left = Node(4)
root.rigth = Node(3)


root.left.left = Node(2)
root.left.rigth = Node(1)
