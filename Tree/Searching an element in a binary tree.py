#To search an elment in a binary tree we can use any tree traversal method such as inorder, preorder or postorder.
#-----------------------------------------------------------------------------------------------------------------
#class to create node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
          
#creating binary tree
def construct_tree(lst, i, n):
    root = None
      
    if i < n:
        root = Node(lst[i])
          
        root.left = construct_tree(lst, 2*i+1, n)
        root.right = construct_tree(lst, 2*i+2, n)
          
    return root

def search_inorder(root, target):
    if root:
        flag1 = search_inorder(root.left, target)
        if flag1 == True:
            return True
        
        if root.value == target:
            return True
        
        flag2 = search_inorder(root.right, target)
        return flag2
    
def search_preorder(root, target):
    if root:
        if root.value == target:
            return True
        flag1 = search_preorder(root.left, target)
        if flag1 == True:
            return True
        
        flag2 = search_preorder(root.right, target)
        return flag2
    
def search_postorder(root, target):
    if root:
        flag1 = search_postorder(root.left, target)
        if flag1 == True:
            return True
        
        flag2 = search_postorder(root.right, target)
        if flag2 == True:
            return True
        
        if root.value == target:
            return True
        


lst = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
n = len(lst)
root = construct_tree(lst, 0, n)
target = 4

a = search_inorder(root, target)
if a == True:
    print("found")
else:
    print("not found")
    
b = search_preorder(root, target)
if b == True:
    print("found")
else:
    print("not found")
    
c = search_postorder(root, target)
if c == True:
    print("found")
else:
    print("not found")
