matrix = [
 [1, 1, 0, 0], # City 0 connects to 1
 [1, 1, 1, 0], # City 1 connects to 0 and 2 (The Bridge)
 [0, 1, 1, 1], # City 2 connects to 1 and 3
 [0, 0, 1, 1]  # City 3 connects to 2
]

visited = [False] * 4


def dfs(node, matrix, visited, n):
    visited[node] = True
    print(node, "-> ", end="")

    for j in range(n):
        if matrix[node][j] == 1 and not visited[j]:
            dfs(j, matrix, visited, n)

dfs(2, matrix, visited, 4)
