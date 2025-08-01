class Solution:
    def tribonacci(self, n: int) -> int:
        seq = [0,1,1]

        if n < 3:
            return seq[n]

        for _ in range(n-2):
            tmp = sum(seq)
            seq[0] = seq[1]
            seq[1] = seq[2]
            seq[2] = tmp
        
        return seq[-1]