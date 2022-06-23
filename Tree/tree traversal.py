#Class to construct nodes
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
         
#constructing a complete binary tree from given array
def construct_tree(lst, i, n):
    root = None
     
    if i < n:
        root = Node(lst[i])
         
        root.left = construct_tree(lst, 2*i+1, n)
        root.right = construct_tree(lst, 2*i+2, n)
         
    return root
 
#preorder traversal
def preorder(root):
    if root:
        print(root.value, end = " ")
        preorder(root.left)
        preorder(root.right)
        
#inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.value, end = " ")
        inorder(root.right)
        
#postorder traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.value, end = " ")
        
 
 
lst = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
n = len(lst)
root = construct_tree(lst, 0, n)
print("preorder traversal: ", end = " ")
preorder(root)
print("\ninorder traversal: ", end = " ")
inorder(root)
print("\npostorder traversal: ", end = " ")
postorder(root)
