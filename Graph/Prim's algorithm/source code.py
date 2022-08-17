#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

def find_source(distance, mstset, v):#-------------------------->function1
    min_val = float("inf")
    index = 0
    for source in range(v):
        if distance[source] < min_val and mstset[source] == False:
            min_val = distance[source]
            index = source
    return index
  
   
def print_mst(parent, distance):#-------------------------------->function2
    print ("Edge \tWeight")
    for i in range(1, v):
        if parent[i] != None:
            print (parent[i], "->", i, "\t", distance[i])
            
   
def prim(v, matrix):#--------------------------------------------->function3
    distance = [float("inf")]*v
    mstset = [False]*v
    parent = [None]*v
     
    distance[0] = 0
    parent[0] = -1
       
    for vertex in range(v):#-------------------------------------->line1
        source = find_source(distance, mstset, v)
        mstset[source] = True
        for neighbor in range(v):
            if matrix[source][neighbor]>0 and mstset[neighbor] == False and distance[neighbor] > matrix[source][neighbor]:
                distance[neighbor] = matrix[source][neighbor]
                parent[neighbor] = source
    print_mst(parent, distance)
      
v = 5
matrix = [[0, 0, 3, 0, 0],    
          [0, 0, 10, 4, 0],    
          [3, 10, 0, 2, 6],    
          [0, 4, 2, 0, 1],    
          [0, 0, 6, 1, 0]]
prim(v, matrix)

#output :
# Edge 	        Weight
# 3 -> 1 	 4
# 0 -> 2 	 3
# 2 -> 3 	 2
# 3 -> 4 	 1

#-----------------------------------------------------------------------------------------------------------------------------------
#1. First we intitalize distance, mstset and parent lists in function3.
#2. Now we preprocess our resources. we will start from the vertex 0 so cost to reach to the vertex 0 will be 0 as we are already there and parent of vertex 0 will be -1.
#3. Now with the help of function1 we will find the vertex that is not visited priviously and has the minimum cost to be reached, and we call it source in function3/line30.
  #Make surce vertex visited in mstset.
#4. Now we will find all those neighbor vertex that is directly connected to the current source vertex and previously not visited.
  #If cost in distance list is(previously calculated cost for neighbor vertex) is greater than the cost from current source vertex to neighbor vertex.
  #Then update the cost of neighbor vertex in distance list.
  #And parent of neighbor vertex will be current source vertex in parent list as now we are reaching to the neighbor vertex from current source vertex.
 #5. Repeat steps 3 to 4 equals to the number of vertex times.
  
  

