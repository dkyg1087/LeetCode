# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # First we find the length n of the linked list
        # We find k mod n to know the exact amount to shift
        # We connect the end to the head to make a circulate linked list
        # we find the correct tail by moving to k-n-1,tail.next will be head and we break the connection to tail to create the new linked list
        
        
        if not head:
            return None
        
        if not head.next:
            return head
        
        length = 1

        cur = head

        while cur.next:
            length += 1
            cur = cur.next
        
        cur.next = head

        shift = k % length

        new_tail = head

        for _ in range(length - shift - 1):
            new_tail = new_tail.next
        
        new_head = new_tail.next

        new_tail.next = None

        return new_head


        