#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

from heapq import *
     
def build_graph(v, edges):
    graph = {}
    for i in range(1, v+1):
        graph[i] = []
             
    for edge in edges:
        graph[edge[0]].append(edge[1])
             
    return graph
     
def build_cost(v, edges):
    cost = {}
    for edge in edges:
        cost[(edge[0], edge[1])] = edge[2]
             
    return cost
             
def dijkstra(v, edges):
    graph = build_graph(v, edges)
    distance = [float("inf")]*(v+1)
    parent = [-1]*(v+1)
    visited = [False]*(v+1)
    cost = build_cost(v, edges)
    min_heap = []
         
    src = 1
    heappush(min_heap, (0, src))
    distance[src] = 0
         
    while min_heap:
        curr_distance, curr_node = heappop(min_heap)
        if visited[curr_node] is False:
            visited[curr_node] = True
            for nbr in graph[curr_node]:
                if  distance[nbr] > curr_distance + cost[(curr_node, nbr)]:
                    distance[nbr] = curr_distance + cost[(curr_node, nbr)]
                    parent[nbr] = curr_node
                    heappush(min_heap, (distance[nbr], nbr))
                         
    print ("Edge \tWeight")
    for i in range(1, v+1):
        print(parent[i], "->", i, "\t",distance[i])
     
v = 4
edges = [[1,2,2],[1,3,9],[1,4,14],[1,3,9],[3,4,2]]
dijkstra(v, edges)

#-----------------
#OUTPUT:
# Edge 	Weight
# -1 -> 1  0
# 1 -> 2 	 2
# 1 -> 3 	 9
# 3 -> 4 	 11
