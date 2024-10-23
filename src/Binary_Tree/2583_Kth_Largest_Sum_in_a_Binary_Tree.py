# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        queue = [root,]
        while len(queue) != 0:
            cur_sum = 0
            temp = []
            for node in queue:
                cur_sum += node.val
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)
            
            if len(heap) < k:
                heapq.heappush(heap,cur_sum)
            else:
                if heap[0] < cur_sum:
                    heapq.heappop(heap)
                    heapq.heappush(heap,cur_sum)

            queue = temp

        return heap[0] if len(heap) >= k else -1
        