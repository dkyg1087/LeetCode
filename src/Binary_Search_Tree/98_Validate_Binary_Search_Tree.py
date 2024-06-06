# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # Traverse the tree in inorder, if its not strictly increaseing then its not a valid BST.
        
        def inorder(root):
            if root:
                yield from inorder(root.left)
                yield root.val
                yield from inorder(root.right)
            
        
        last_node = None

        for val in inorder(root):
            if last_node is not None:
                if last_node >= val:
                    return False
                last_node = val
            else:
                last_node = val
        
        return True
            

        
