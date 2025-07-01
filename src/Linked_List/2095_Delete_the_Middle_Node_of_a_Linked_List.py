# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next is None:
            return None
        
        p1 = head
        p2 = head
        p1_last = None

        while not (p2 is None or p2.next is None):
            p1_last = p1
            p1 = p1.next
            p2 = p2.next.next
            
        p1_last.next = p1.next

        return head