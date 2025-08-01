# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        
        # Treat this as sorting the a single linked list into two linked list
        # After sorting it into 2 we just combine the two and form the new one
        
        if not head or not head.next:
            return head
        
        head_dummy = ListNode()
        head_cur = head_dummy

        anchor_dummy = ListNode()
        anchor_cur = anchor_dummy
        
        cur = head

        while cur:
            if cur.val < x:
                head_cur.next = cur
                head_cur = head_cur.next
            else:
                anchor_cur.next = cur
                anchor_cur = anchor_cur.next
            nextt = cur.next
            cur.next = None
            cur = nextt
        
        head_cur.next = anchor_dummy.next

        return head_dummy.next
                
        