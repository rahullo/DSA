# from Tree.treeimplementation import BinarySearchTree
# from Tree.treeimplementation import print2D

import Tree.treeimplementation as tree

# binary = tree.BinarySearchTree()
# binary.insert(4)
# binary.insert(8)
# binary.insert(2)
# binary.insert(3)
# binary.insert(1)
# binary.insert(0)
# binary.insert(-1)
# binary.insert(10)
# binary.insert(13)

bin1 = tree.BinarySearchTree()
bin1.insert(6)
bin1.insert(3)
bin1.insert(9)
bin1.insert(7)
bin1.insert(10)
bin1.insert(1)
bin1.insert(4)

bin2 = tree.BinarySearchTree()
bin2.insert(6)
bin2.insert(3)
bin2.insert(9)
bin2.insert(7)
bin2.insert(10)
bin2.insert(0)
bin2.insert(4)


# tree.print2D(binary.root)
# print(tree.traverseInOrder(binary.root, []))
# print(tree.traversepostOrder(binary.root, []))
# print(tree.traversepreOrder(binary.root, []))

# breadthFirstSearch() {
#         let currentNode = this.root;
#         let list = [];
#         let queue = [];
#         queue.push(currentNode)
#         while (queue.length > 0) {
#             currentNode = queue.shift();

#             list.push(currentNode.value);
#             if (currentNode.left) {
#                 queue.push(currentNode.left);
#             }
#             if (currentNode.right) {
#                 queue.push(currentNode.right);
#             }
#         }
#         return list;

# def bfs(root):
#     currNode = root
#     stack = []
#     ans = []
#     stack.append(root)

#     while len(stack) > 0:
#         currNode = stack[0]
#         ans.append(currNode.value)
#         if currNode.left:
#             stack.append(currNode.left)
#         if (currNode.right):
#             stack.append(currNode.right)
#         del stack[0]
#     return ans

# def dfs(root, ans):
#     currNode = root
#     ans.append(currNode.value)
#     if currNode.left:
#         dfs
        
#     return ans
# print(bfs(binary.root))
# print(dfs(binary.root))

def isSameTree(p, q):
        if not p or not q:
            return p == q
        return p.value == q.value and isSameTree(p.left, q.left) and isSameTree(p.right, q.right)

# def searchTraverse(p, q):N


tree.print2D(bin1.root)
print("########)")
tree.print2D(bin2.root)
print(isSameTree(bin1.root, bin2.root))