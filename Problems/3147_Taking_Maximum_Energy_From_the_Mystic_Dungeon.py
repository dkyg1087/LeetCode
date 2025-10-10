class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        max_energy = -math.inf

        window = [0] * k

        idx = 0 if len(energy) % k == 0 else (len(energy)%k) -1 

        for i in range(len(energy) -1 , -1 ,-1):
            window[idx] += energy[i]
            max_energy = max(max_energy,window[idx])
            idx -= 1
            if idx == -1:
                idx = k-1
            #print(window)
        return max_energy