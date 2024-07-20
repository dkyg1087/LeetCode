# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        # Do a preorder traverse taking note of the current tail
        # Store the right part of the tree because we will be replacing it.
        
        def preorder_stitch(node,tail):

            # edge case
            if node is None:
                return tail

            temp = node.right
            tail.right = node
            tail.left = None
            tail = tail.right
            new_tail = preorder_stitch(node.left,tail)
            new_tail = preorder_stitch(temp,new_tail)
            return new_tail
        
        dummy = TreeNode(right=root)
        preorder_stitch(root,dummy)


            
            