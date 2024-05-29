# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        
        # Inorder traverse the full tree
        # Save the last node value to compare with the current one
        # Return the min difference

        def inorder_traverse(root):
            if root is not None:
                yield from inorder_traverse(root.left)
                yield root.val
                yield from inorder_traverse(root.right)
        
        min_diff = 100000
        
        last = None

        for node_val in inorder_traverse(root):

            if last is not None:
                
                min_diff = min(node_val - last,min_diff)
                last = node_val 
            else:
                last = node_val
        
        return min_diff


