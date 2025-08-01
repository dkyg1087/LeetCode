# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # Do a slow fast pointer approach
        # The fast pointer is n ahead of the slow pointer
        # If the fast pointer hits the end(None), we know the slow pointer is on the one we need to delete
        # save the previous one as well to connect the rest

        if not head:
            return None
        
        dummy = ListNode(next=head)

        prev = dummy
        slow = dummy.next
        fast = dummy.next

        for _ in range(n):
            fast = fast.next if fast.next else None

        while fast:
            prev = prev.next
            slow = slow.next
            fast = fast.next if fast.next else None
        
        prev.next = slow.next

        return dummy.next



            

        
        

        