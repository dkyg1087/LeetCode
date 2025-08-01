# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        # Just make one pass from the linked list and store the last seen and compare with previous
        # Create a dummy node to deal with edge cases

        if not head:
            return None
        
        dummy = ListNode(val = -101 ,next = head)
        store = None
        prev = dummy
        cur = dummy.next
        delete = False
        
        while prev:

            if cur is None or prev.val != cur.val:
                if delete:
                    store.next = cur
                    delete = False
                else:
                    store = prev
            else:
                delete = True
            prev = cur
            cur = cur.next if cur else None
        
        return dummy.next