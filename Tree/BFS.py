from tree import treeNode

tree1 = treeNode(5)

tree1.left = treeNode(3)
tree1.right = treeNode(7)

tree1.left.left = treeNode(1)
tree1.left.right = treeNode(4)


tree1.right.left = treeNode(1)
tree1.right.right = treeNode(4)


def BFS(root):
    if not root:
        return None
    nodes = [root]

    while nodes:
        current_node = nodes.pop()
        print(current_node.val, end=", ")
        if current_node.left:
            nodes.append(current_node.left)
        if current_node.right:
            nodes.append(current_node.right)


BFS(tree1)