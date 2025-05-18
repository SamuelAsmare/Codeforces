from collections import defaultdict
m,n = list(map(int,input().split()))
arr = [list(map(int,input().split())) for _ in range(n)]
graph = defaultdict(list)  
visited , ans = set() , 0
def dfs(graph,e,visited):
    if e in visited:
        return 
    visited.add(e)
    for j in graph[e]:
        if(len(graph[j]) <= 1):
             dfs(graph,j,visited)

for u, v in arr:
    graph[u].append(v)
    graph[v].append(u)
for i in graph:
    if(len(graph[i]) <= 1):
        dfs(graph,i , visited)
        if i in visited:
            ans +=1
        
print (ans)
