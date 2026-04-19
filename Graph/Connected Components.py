
adj = [[1,0,0],[0,1,0],[0,0,1]]
n = 3


def dfs(node, adj, visited):
    visited[node] = True
    print(node, end=" ")

    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj, visited)


visited = [False] * n
dfs(0, adj, visited)
print("\n")
visited = [False] * n
dfs(2, adj, visited)
print("\n")
visited = [False] * n
dfs(1, adj, visited)
print("\n")


def count_components(n, adj):
    visited = [False] * n
    count = 0

    for i in range(n):
        if not visited[i]:
            dfs(i, adj, visited)
            count += 1

    return count

print("\n", "Connected Components", count_components(n, adj))