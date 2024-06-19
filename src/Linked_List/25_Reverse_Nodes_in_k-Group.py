# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Use slow fast pointers to enssure there is enough nodes to reverse
        # as soon as we find enough nodes we reverse it

        def reverse_k_and_return_last(head_ptr,k):
            end = head_ptr.next
            cur_node = head_ptr.next
            next_node = cur_node.next
            for _ in range(k-1):
                next_node = cur_node.next
                cur_node.next,next_node.next,head_ptr.next = next_node.next,head_ptr.next,next_node
            return end


        dummy_head = ListNode(next = head)

        slow = fast = dummy_head
        counter = 0

        while fast:
            if counter == 0:
                fast = slow
                counter += 1
                fast = fast.next
            elif counter == k:
                slow = reverse_k_and_return_last(slow,k)
                counter = 0
            else:
                counter += 1
                fast = fast.next
            
        return dummy_head.next
            
        
            