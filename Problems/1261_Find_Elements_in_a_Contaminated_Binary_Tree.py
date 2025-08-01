# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.ref_dict = {}
    
        def traverse(node):
            if node.left:
                node.left.val = node.val * 2 + 1
                self.ref_dict[node.val * 2 + 1] = True
                traverse(node.left)
            if node.right:
                node.right.val = node.val * 2 + 2
                self.ref_dict[node.val * 2 + 2] = True
                traverse(node.right)

            return

        if root:
            root.val = 0
            self.ref_dict[0] = True
            traverse(root)
        return


    def find(self, target: int) -> bool:
        return target in self.ref_dict


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)