class Solution:
    def countNodes(self, root) -> int:
        if not root:
            return 0
        
        left_h = self.get_left_height(root)
        right_h = self.get_right_height(root)
        
        # If left and right heights are the same, it's a perfect binary tree
        if left_h == right_h:
            return (2 ** left_h) - 1
        
        # Otherwise, recursively count nodes
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

    def get_left_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.left
        return height

    def get_right_height(self, node):
        height = 0
        while node:
            height += 1
            node = node.right
        return height