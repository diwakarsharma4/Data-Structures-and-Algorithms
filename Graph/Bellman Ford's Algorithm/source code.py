#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

def bellman_ford(v, edges):
    distance = [float("inf")]*(v)
    src = 0
    distance[src] = 0
    
    for i in range(v-1):
        for edge in edges:
            source, destination, cost = edge
            if distance[source] != float("inf") and distance[source] + cost < distance[destination]:
                distance[destination] = distance[source] + cost
                
    for edge in edges:
        source, destination, cost = edge
        if distance[source] != float("inf") and distance[source] + cost < distance[destination]:
            return
    
    print("source"," destination","\t","cost")
    for i in range(v):
        print(src,"  -->  ",i,"\t\t",distance[i])
     
v = 5
edges = [[0,1,5],[0,2,4],[1,3,3],[2,1,6],[3,2,2]]
bellman_ford(v, edges)

#------------------------------------------------
#OUTPUT:
# source  destination 	 cost
# 0   -->   0 		        0
# 0   -->   1 		        5
# 0   -->   2 		        4
# 0   -->   3 		        8
# 0   -->   4 		        inf
