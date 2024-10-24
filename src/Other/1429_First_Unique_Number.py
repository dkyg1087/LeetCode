class FirstUnique:
    class LL_Node:
        def __init__(self,num,prev_node=None,next_node=None):
            self.val = num
            self.prev = prev_node
            self.next = next_node
    
    def __init__(self, nums: List[int]):
            self.dummy_head = self.LL_Node(-1)
            self.dummy_tail = self.LL_Node(-1)
            self.dummy_head.next = self.dummy_tail
            self.dummy_tail.prev = self.dummy_head
            self.unique_dict = {}

            for num in nums:
                self.add(num)

    def showFirstUnique(self) -> int:
        if self.dummy_head.next == self.dummy_tail:
            return -1
        else:
            return self.dummy_head.next.val 
    def add(self, value: int) -> None:
        if value not in self.unique_dict:
            temp = self.LL_Node(value,None,self.dummy_tail)
            self.unique_dict[value] = temp
            temp.prev = self.dummy_tail.prev
            self.dummy_tail.prev = temp
            temp.prev.next = temp
        else:
            if self.unique_dict[value] == -1:
                return
            else:
                del_node = self.unique_dict[value]
                del_node.prev.next = del_node.next
                del_node.next.prev = del_node.prev
                self.unique_dict[value] = -1
                del del_node
            

        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)