"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        # iterate through the current level using "next" to construct the next "linked list"
        # If the current "linked list" hits None go to the constructed next "linked list" with next_head
        # repeat until None

        cur = None
        next_head = root
        next_tail = None

        while next_head is not None:
            cur = next_head
            next_head = next_tail = None
            while cur is not None:
            
                if cur.left:
                    if next_head is None:
                        next_head = cur.left
                        next_tail = cur.left
                    else:
                        next_tail.next = cur.left
                        next_tail = next_tail.next
                if cur.right:
                    if next_head is None:
                        next_head = cur.right
                        next_tail = cur.right
                    else:
                        next_tail.next = cur.right
                        next_tail = next_tail.next
                
                cur = cur.next

        return root

            

        
        

