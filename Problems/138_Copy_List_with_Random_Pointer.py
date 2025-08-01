"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        # The easy way of doing this is just to hash the node into a dictionary and run through the linklist through random and next
        
        # The current one first creates the coppied node right after the original one
        # By doing that we know what to save in our new nodes'  random pointers
        # Because we can just access the old nodes' random pointer to know where it is pointing to and update accordingly 

        cur = head

        if not cur:
            return None

        while cur:
            temp_node = Node(cur.val,None,None)
            temp_node.next = cur.next
            cur.next = temp_node
            cur = temp_node.next

        cur = head

        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        
        res = head.next
        old_cur = head
        new_cur = head.next
        while old_cur:
            old_cur.next = old_cur.next.next
            new_cur.next = new_cur.next.next if new_cur.next else None

            old_cur = old_cur.next
            new_cur = new_cur.next
         
        
        return res



        
        
            
        