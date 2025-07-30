class MyCircularDeque:

    def __init__(self, k: int):
        self.dequeue = [-1]*k
        self.size = 0
        self.max = k
        self.front = -1
        self.back = -1

    def insertFront(self, value: int) -> bool:
        if self.size == self.max:
            return False
        if self.front != -1:
            idx = ((self.front - 1) + 2 * self.max) % self.max
        else:
            idx = 0
            self.back = idx

        self.front = idx
        self.dequeue[idx] = value
        self.size += 1

        return True

    def insertLast(self, value: int) -> bool:
        if self.size == self.max:
            return False
        if self.back != -1:
            idx = ((self.back + 1) + 2 * self.max) % self.max
        else:
            idx = 0
            self.front = idx

        self.back = idx
        self.dequeue[idx] = value
        self.size += 1

        return True

    def deleteFront(self) -> bool:
        if self.size == 0:
            return False
            
        self.size -= 1
        self.dequeue[self.front] = -1
        self.front = ((self.front + 1) + 2 * self.max) % self.max

        if self.size == 0:
            self.front = -1
            self.back = -1
        
        return True

    def deleteLast(self) -> bool:
        if self.size == 0:
            return False
        
        self.size -= 1
        self.dequeue[self.back] = -1
        self.back = ((self.back - 1) + 2 * self.max) % self.max
        
        if self.size == 0:
            self.front = -1
            self.back = -1
            
        return True

    def getFront(self) -> int:
        return -1 if self.size == 0 else self.dequeue[self.front]

    def getRear(self) -> int:
        return -1 if self.size == 0 else self.dequeue[self.back]

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.max
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()