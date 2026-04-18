n = 5
edges = [[0,1], [0,2], [1,3], [2,4]]

container = [[] for i in range(n)]

def adjacencyList(container, edges):
    for u, v in edges:
        container[u].append(v)
        container[v].append(u)

adjacencyList(container, edges)

for _ in range(n):
    print(_, "--> " , container[_])
