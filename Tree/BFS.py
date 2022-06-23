#In breadth first search we iterate level by level in a binary tree.
#For BFS we use queue data structure.
#-------------------------------------------------------------------------------------------
#To print node values in level order

#Class to create node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
          
#constructing tree
def construct_tree(lst, i, n):
    root = None
      
    if i < n:
        root = Node(lst[i])
          
        root.left = construct_tree(lst, 2*i+1, n)
        root.right = construct_tree(lst, 2*i+2, n)
          
    return root

#bfs execution
def bfs(root):
    if root:
        que = []
        que.append(root)
        
        while len(que) > 0:
            que_length = len(que)
            for node in que:
                print(node.value, end = " ")
            
            while que_length > 0:
                current_node = que.pop(0)
                if current_node.left is not None:
                    que.append(current_node.left)
                if current_node.right is not None:
                    que.append(current_node.right)
                que_length -= 1

lst = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
n = len(lst)
root = construct_tree(lst, 0, n)
bfs(root)

#OUTPUT--> 1 2 3 4 5 6 7 8 9 10
#--------------------------------------------------------------------------------
#To print all nodes level by level

#Class to create node
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
          
#constructing tree
def construct_tree(lst, i, n):
    root = None
      
    if i < n:
        root = Node(lst[i])
          
        root.left = construct_tree(lst, 2*i+1, n)
        root.right = construct_tree(lst, 2*i+2, n)
          
    return root

#bfs execution
def bfs(root):
    if root:
        que = []
        que.append(root)
        
        while len(que) > 0:
            que_length = len(que)
            current_level_nodes = []
            for node in que:
                current_level_nodes.append(node.value)
            ans.append(current_level_nodes.copy())
            
            while que_length > 0:
                current_node = que.pop(0)
                if current_node.left is not None:
                    que.append(current_node.left)
                if current_node.right is not None:
                    que.append(current_node.right)
                que_length -= 1

ans = []
lst = [1, 2, 3, 4, 5, 6, 7, 8 , 9, 10]
n = len(lst)
root = construct_tree(lst, 0, n)
bfs(root)
print(ans)

#OUTPUT --> [[1], [2, 3], [4, 5, 6, 7], [8, 9, 10]]
