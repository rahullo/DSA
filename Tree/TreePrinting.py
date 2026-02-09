from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(root):
    if not root:
        print("Empty tree")
        return

    queue = deque([root])

    while queue:
        level_size = len(queue)
        level = []

        for _ in range(level_size):
            node = queue.popleft()
            if node:
                level.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                level.append(None)

        # Stop printing when all nodes are None
        if all(v is None for v in level):
            break

        print(level)


def build_tree(height):
    if height == 0:
        return None

    root = TreeNode(1)
    queue = [root]
    current_val = 2

    for _ in range(height - 1):
        next_level = []
        for node in queue:
            node.left = TreeNode(current_val)
            current_val += 1
            node.right = TreeNode(current_val)
            current_val += 1
            next_level.extend([node.left, node.right])
        queue = next_level

    return root
