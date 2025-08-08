class SmallestInfiniteSet:

    def __init__(self):
        self.global_count = 1
        self.added_num = []
        self.present = set()

    def popSmallest(self) -> int:
        if len(self.added_num) == 0:
            self.global_count += 1
            return self.global_count - 1
        else:
            popped = heapq.heappop(self.added_num)
            self.present.remove(popped)
            return popped

    def addBack(self, num: int) -> None:
        if self.global_count > num and (num not in self.present):
            self.present.add(num)
            heapq.heappush(self.added_num,num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)