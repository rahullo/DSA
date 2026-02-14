
def hasPathSum(root, targetSum) -> bool:
    if not root:
        return False
    
    # Check if we are at a leaf node
    if not root.left and not root.right:
        return root.val == targetSum
    
    # Update the target for the children
    new_sum = targetSum - root.val
    
    # If either the left or right subtree returns True, the path exists
    return hasPathSum(root.left, new_sum) or \
            hasPathSum(root.right, new_sum)