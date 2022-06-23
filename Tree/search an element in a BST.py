#To search an element in a BST we will use recursive approach.
#-----------------------------------------------------------------------
#class to create node
class Node:
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
        
#creating BST           
def construct_tree(root, value):
    if root.value:
        if value < root.value:
            if root.left == None:
                root.left = Node(value)
            else:
                construct_tree(root.left, value)
        elif value > root.value:
            if root.right == None:
                root.right = Node(value)
            else:
                construct_tree(root.right, value)
    else:
        root.value = value

#searching
def search(root, target):
    if root == None:
        return False
    if root.value == target:
        return True
    if root.value < target:
        return search(root.right, target)
    return search(root.left, target)    
         
    
lst = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
root = Node()

for value in lst:
    construct_tree(root, value)
    
ans = search(root, 6)

if ans == True:
    print("found")
else:
    print("not found")
