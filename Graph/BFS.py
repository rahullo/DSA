from collections import deque

# ---------- INPUT ----------

adj = [[1, 2], [0, 3, 4], [0, 5, 6], [1], [1, 7], [2, 8], [2], [4, 8], [5, 7]]
n, m = 9, 9

print(adj)
# ---------- BFS ----------
def bfs(start):
    visited = [False] * n
    q = deque()

    visited[start] = True
    q.append(start)

    while q:
        node = q.popleft()
        print(node, end=" ")

        for neighbor in adj[node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                q.append(neighbor)


# ---------- DFS ----------
def dfs(node, visited):
    visited[node] = True
    print(node, end=" ")
    

    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited)


# ---------- RUN ----------
print("BFS:")
bfs(0)
print("\nDFS:")
visited = [False] * n
dfs(0, visited)