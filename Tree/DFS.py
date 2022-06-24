#In binary tree DFS is actually inorder traversal.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
          
def construct_tree(lst, i, n):
    root = None
      
    if i < n:
        root = Node(lst[i])
          
        root.left = construct_tree(lst, 2*i+1, n)
        root.right = construct_tree(lst, 2*i+2, n)
          
    return root

#dfs execution
def dfs(root):
    if root:
        dfs(root.left)
        print(root.value, end = " ")
        dfs(root.right)

lst = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
n = len(lst)
root = construct_tree(lst, 0, n)
dfs(root) 

#OUTPUT--> 8 4 9 2 10 5 1 6 3 7 
 
#------------------------------------------------------------------------

#DFS iterative approach using stack.

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
            
def construct_tree(lst, i, n):
    root = None
        
    if i < n:
        root = Node(lst[i])
            
        root.left = construct_tree(lst, 2*i+1, n)
        root.right = construct_tree(lst, 2*i+2, n)
            
    return root
 
def dfs(root):
    if root:
        stack = []
        current_node = root
        while stack or current_node:
            if current_node:
                stack.append(current_node)
                current_node = current_node.left
            else:
                current_node = stack.pop()
                print(current_node.value, end = " ")
                current_node = current_node.right
 
lst = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
n = len(lst)
root = construct_tree(lst, 0, n)
dfs(root)

#OUTPUT--> 8 4 9 2 10 5 1 6 3 7 
