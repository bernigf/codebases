class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    # BASE CASE: If the node is None, we've reached beyond a leaf.
    # A non-existent tree has a depth of 0.
    if not root:
        return 0
    
    # RECURSIVE STEP: If the node exists, we ask its children for their heights.
    
    # We call the function again for the left subtree.
    # This will keep going down until it hits a None (Base Case).
    left_height = maxDepth(root.left)
    
    # We do the same for the right subtree.
    right_height = maxDepth(root.right)
    
    # COMBINE STEP: The height of the current node is 1 (itself) 
    # plus the height of the tallest child.
    # We use max() to choose the longest path.
    return max(left_height, right_height) + 1

def sumElements(root):
    # BASE CASE: An empty node contributes 0 to the total sum.
    if not root:
        return 0

    # RECURSIVE STEP: The total sum for the current "root" is:
    # Its own value + the sum of everything on the left + the sum of everything on the right.
    
    # We call the function for both children.
    left_sum = sumElements(root.left)
    right_sum = sumElements(root.right)

    # COMBINE: Return the sum of the current node's value and its subtrees.
    return root.val + left_sum + right_sum

# Creating a simple tree:
#      1
#     / \
#    2   3

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Test Sum:
print(f"Total Sum: {sumElements(root)}") # Output: 6

# Test Invert:
inverted = invertTree(root)
print(f"New Root Left: {inverted.left.val}") # Output: 3 (instead of 2)
