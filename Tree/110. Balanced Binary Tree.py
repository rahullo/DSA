from tree import treeNode

tree1 = treeNode(5)

tree1.left = treeNode(3)
tree1.right = treeNode(7)

tree1.left.left = treeNode(1)
tree1.left.right = treeNode(4)


tree1.right.left = treeNode(6)
tree1.right.right = treeNode(8)



def isBalanced(root):
    def height(node):
        if not node:
            return 0

        left = height(node.left)
        if left == -1:
            return -1

        right = height(node.right)
        if right == -1:
            return -1
        print("Left: ", left,", Right: ", right)
        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)

    return height(root) != -1
        
print(isBalanced(tree1))