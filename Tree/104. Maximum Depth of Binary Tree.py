class Solution:
    def maxDepth(self, root):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


from tree import treeNode

tree1 = treeNode(5)

tree1.left = treeNode(3)
tree1.right = treeNode(7)

tree1.left.left = treeNode(1)
tree1.left.right = treeNode(4)


tree1.right.left = treeNode(1)
tree1.right.right = treeNode(4)

tr = Solution()
print(tr.maxDepth(tree1))