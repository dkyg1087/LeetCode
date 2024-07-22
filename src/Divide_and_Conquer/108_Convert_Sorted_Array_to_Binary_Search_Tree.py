class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def constructTree(numsList):
            length = len(numsList)

            if not numsList:
                return None
            elif length == 1:
                return TreeNode(numsList[0])
            
            mid = length // 2
            midNode = TreeNode(numsList[mid])
        
            midNode.left = constructTree(numsList[:mid])
            midNode.right = constructTree(numsList[mid+1:])

            return midNode
        
        return constructTree(nums)
            