#author- Diwakar Sharma [Github- diwakarsharma4]
#-----------------------------------------------

def topological(v, edges):
    ans = []
    if v<=0:
        return ans
       
    graph = {}
    for i in range(v):
        graph[i] = []
           
    indegree = {}
    for i in range(v):
        indegree[i] = 0
       
    for edge in edges:
        parent = edge[0]
        child = edge[1]
        indegree[child] += 1
        graph[parent].append(child)
           
    que = []
    for i in indegree:
        if indegree[i] == 0:
            que.append(i)
               
    while que:
        node = que.pop(0)
        ans.append(node)
           
        for neighb in graph[node]:
            indegree[neighb] -= 1
               
            if indegree[neighb] == 0:
                que.append(neighb)
                   
    if len(ans)!=v:
        return []
               
    return ans
       
v = 7
edges = [[5, 3], [5, 4], [6, 4], [6, 2], [4, 1], [3, 0], [3, 1], [3, 2]]
ans = topological(v, edges)
print(ans)
#--------------------------------------------------------------------------
#OUTPUT:
# [5, 6, 3, 4, 0, 2, 1]
