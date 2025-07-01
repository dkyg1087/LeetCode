# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        ll = []

        tmp = head

        while tmp:
            ll.append(tmp.val)
            tmp = tmp.next
        
        half = len(ll) // 2

        maxx = 0

        for i in range(half):
            maxx = max(ll[i]+ll[-1*(i+1)],maxx)
        
        return maxx