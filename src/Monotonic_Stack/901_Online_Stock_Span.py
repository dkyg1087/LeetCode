class StockSpanner:

    def __init__(self):
        self.monoStk = []

    def next(self, price: int) -> int:
        ans = 1
        while len(self.monoStk) > 0 and self.monoStk[-1][0] <= price:
            ans += self.monoStk.pop()[1]
        self.monoStk.append((price,ans))
        return ans
            


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)