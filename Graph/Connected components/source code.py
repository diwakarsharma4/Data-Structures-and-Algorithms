#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------
#print all connected components
def build_graph(v, edges):
    graph = {}
    for i in range(1, v+1):
        graph[i] = []
          
    for edge in edges:
        src = edge[0]
        dst = edge[1]
          
        graph[src].append(dst)
        graph[dst].append(src)
          
    return graph
  
def dfs(node, graph, visited, sublist):
    visited[node] = True
    sublist.append(node)
      
    for vertex in graph[node]:
        if visited[vertex] == False:
            sublist = dfs(vertex, graph, visited, sublist)
              
    return sublist
  
def connected_components(v, edges):
    visited = [False]*(v+1)
    graph = build_graph(v, edges)
    for node in range(1, v+1):
        if visited[node] == False:
            edge_list.append(dfs(node, graph, visited, []))
   
      
v = 5
# edges = [[1,2], [1,3], [2,3], [1,4]]
edges = [[2, 1], [3, 4], [4, 5]]
edge_list = []
connected_components(v, edges)
print(edge_list)

#------------------------
#OTPUT:
# [[1, 2], [3, 4, 5]]
#-------------------------------------------------------------------
#count number of connected components

def build_graph(v, edges):
    graph = {}
    for i in range(v+1):
        graph[i] = []
          
    for edge in edges:
        src = edge[0]
        dst = edge[1]
          
        graph[src].append(dst)
        graph[dst].append(src)
          
    return graph    
  
def dfs(node, graph, visited):
    visited[node] = True
    for vertex in graph[node]:
        if visited[vertex] == False:
            dfs(vertex, graph, visited)
                
def connected_components(v, edges):
    visited = [False]*(v+1)
    graph = build_graph(v, edges)
    count = 0
    
    for node in range(v+1):
        if visited[node] == False:
            dfs(node, graph, visited)
            count += 1
    
    return count
   
n, m = list(map(int, input().split())) #n = number of nodes, m = number or edges
edges = []
for i in range(m):
    a, b = list(map(int, input().split()))
    edges.append([a, b])

ans = connected_components(n, edges)
print(ans-1)
