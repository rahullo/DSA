# Definition for a binary tree node.
import TreePrinting as tp

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums):
        def build(l, r):
            if l > r:
                return None

            mid = (l + r) // 2
            root = TreeNode(nums[mid])
            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)
            return root

        return build(0, len(nums) - 1)

        


tr = Solution()

root = tr.sortedArrayToBST([-10, -3, 0, 4, 9])

tp.print_tree(root)
