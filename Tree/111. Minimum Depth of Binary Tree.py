from collections import deque
from tree import treeNode

tree1 = treeNode(5)

tree1.left = treeNode(3)
tree1.right = treeNode(7)

tree1.left.left = treeNode(1)
tree1.left.right = treeNode(4)


tree1.right.left = treeNode(6)
tree1.right.right = treeNode(8)




# def minDepth(root):
#     if not root:
#         return 0
    
#     nodes = deque()
#     h = 1
#     while nodes:
#         currentNode = nodes.popleft()

#         if not currentNode.left and currentNode.right:
#             h += 1
#         elif currentNode.left:
#             nodes.append(currentNode.left)
#         elif currentNode.right:
#             nodes.append(currentNode.right)
#     return h

def minDepth(root):
    if not root:
        return 0

    # If one child is missing, go through the other
    if not root.left:
        return 1 + minDepth(root.right)
    if not root.right:
        return 1 + minDepth(root.left)

    # Both children exist
    return 1 + min(
        minDepth(root.left),
        minDepth(root.right)
    )



print(minDepth(tree1))