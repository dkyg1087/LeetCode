# Definition for polynomial singly-linked list.
# class PolyNode:
#     def __init__(self, x=0, y=0, next=None):
#         self.coefficient = x
#         self.power = y
#         self.next = next

# Two pointer just run through two list a the same time like merge sort


class Solution:
    def addPoly(self, poly1: 'PolyNode', poly2: 'PolyNode') -> 'PolyNode':
        p1,p2 = poly1,poly2
        dummy_head = PolyNode()
        cur = dummy_head
        while p1 is not None or p2 is not None:
            if p1 is None:
                cur.next = PolyNode(p2.coefficient,p2.power)
                p2 = p2.next
                cur = cur.next
            elif p2 is None:
                cur.next = PolyNode(p1.coefficient,p1.power)
                p1 = p1.next
                cur = cur.next
            else:
                if p1.power > p2.power:
                    cur.next = PolyNode(p1.coefficient,p1.power)
                    p1 = p1.next
                    cur = cur.next
                elif p1.power < p2.power:
                    cur.next = PolyNode(p2.coefficient,p2.power)
                    p2 = p2.next
                    cur = cur.next
                else:
                    total = p1.coefficient + p2.coefficient
                    if total == 0:
                        p1 = p1.next
                        p2 = p2.next
                        continue
                    else:
                        cur.next = PolyNode(total,p1.power)
                        p1 = p1.next
                        p2 = p2.next
                        cur = cur.next

        return dummy_head.next


        
        