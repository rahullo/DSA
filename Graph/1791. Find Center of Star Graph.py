def findCenter(edges: list[list[int]]) -> int:
    # Get the two nodes from the first edge
    first_node = edges[0][0]
    second_node = edges[0][1]
    
    # Check if the first node exists in the second edge
    if first_node == edges[1][0] or first_node == edges[1][1]:
        return first_node
    else:
        # If it wasn't the first node, it MUST be the second node
        return second_node

print(findCenter([[1,2],[2,3],[4,2]]))

print(findCenter([[7, 4], [8, 4], [4, 9], [4, 1], [2, 4], [4, 3], [5, 4], [4, 6],  [10, 4]])) #4

print(findCenter([[12, 5], [6, 12], [12, 7], [8, 12],[1, 12], [12, 2], [3, 12], [4, 12],  [9, 12], [12, 10], [11, 12], [13, 12], [12, 14], [15, 12]]))#12