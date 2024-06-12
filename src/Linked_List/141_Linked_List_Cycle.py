# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        # Utilize the floyd algorithm(tortise and hare) one travels two times faster to iterate the link list
        # If there is a cycle somewhere, at one point tortise and hare would be at the same spot
        # If hare runs into the void we know there's no cycle 

        tort = hare = head

        while hare:

            hare = hare.next
            if not hare:
                return False
            else:
                hare = hare.next
            
            tort = tort.next

            if tort == hare:
                return True
            
        return False 

        
        