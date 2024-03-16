class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            self.insert_recursiceve(self.root, val)

    def insert_recursiceve(self, node,  val):
        if val < node.val:
            if node.left:
                self.insert_recursiceve(node.left, val)
            else:
                node.left = Node(val)
        else:
            if node.right:
                self.insert_recursiceve(node.right, val)
            else:
                node.right = Node(val)
            

    def BFS(self):
        arr = []
        arr.append(self.root)
        ans = []
        while len(arr):
            current = arr[0]
            del arr[0]
            ans.append(current.val)
            if(current.left):
                arr.append(current.left)
            elif current.right:
                arr.append(current.right)
            print(len(arr))
        return ans
    
    def inorder_traversal(self):
        return self._inorder_traversal_recursive(self.root)

    def _inorder_traversal_recursive(self, node):
        result = []
        if node:
            result.extend(self._inorder_traversal_recursive(node.left))
            result.extend(self._inorder_traversal_recursive(node.right))
            result.append(node.val)
        return result

tree = BinaryTree()
tree.insert(8)
tree.insert(4)
tree.insert(12)
tree.insert(6)
tree.insert(10)
tree.insert(2)
tree.insert(14)

print(tree.inorder_traversal())