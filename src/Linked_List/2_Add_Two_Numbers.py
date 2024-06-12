# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # A simple addition with linked list, keep a carry unit to represent the carry when we add the two nodes
    

        res,cur = None,None

        l1_iter,l2_iter = l1,l2

        carry = None


        while l1_iter or l2_iter or carry:
            
            temp_a = l1_iter.val if l1_iter else 0
            temp_b = l2_iter.val if l2_iter else 0
            temp_c = carry if carry else 0
            
            temp_sum = temp_a + temp_b + temp_c

            if temp_sum >= 10:
                carry = 1
            else:
                carry = None
            
            temp_sum %= 10
            temp_node = ListNode(val = temp_sum)
            
            if res:
                cur.next = temp_node
                cur = cur.next
            else:
                res = temp_node
                cur = res


            l1_iter = l1_iter.next if l1_iter else l1_iter
            l2_iter = l2_iter.next if l2_iter else l2_iter

        return res
        