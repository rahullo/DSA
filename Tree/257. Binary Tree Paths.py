class Solution:
    def binaryTreePaths(self, root):
        res = []
        
        def dfs(node, path):
            if not node:
                return
            
            # Append current node to the path
            path += str(node.val)
            
            # If it's a leaf, save the path
            if not node.left and not node.right:
                res.append(path)
            else:
                # If not a leaf, continue DFS with the arrow
                path += "->"
                dfs(node.left, path)
                dfs(node.right, path)
        
        dfs(root, "")
        return res