# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        # The idea is if you can find one of each in the left and right of the current tree, the current root is the LCA
        # In the case both of the nodes are in one of the side, the recursion will find the LCA, while the other side would return None
        
        if root in (None,p,q):
            return root
        
        left = self.lowestCommonAncestor(root.left,p,q)
        right = self.lowestCommonAncestor(root.right,p,q)

        if left and right:
            return root
        else:
            return left if left else right
    

        