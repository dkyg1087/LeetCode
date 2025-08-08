class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        
        left_heap = []
        right_heap = []
        left_idx = 0
        right_idx = len(costs) - 1
        cost = 0

        for _ in range(candidates):
            if left_idx < len(costs):
                heapq.heappush(left_heap,costs[left_idx])
                left_idx += 1
            else:
                break
        
        for _ in range(candidates):
            if right_idx >= 0 and left_idx <= right_idx:
                heapq.heappush(right_heap,costs[right_idx])
                right_idx -= 1
            else:
                break
        
        for _ in range(k):
            left_min = left_heap[0] if len(left_heap) != 0 else math.inf
            right_min = right_heap[0] if len(right_heap) != 0 else math.inf
            if left_min <= right_min:
                cost += heapq.heappop(left_heap)
                if left_idx <= right_idx and left_idx < len(costs):
                    heapq.heappush(left_heap,costs[left_idx])
                    left_idx += 1
            else:
                cost += heapq.heappop(right_heap)
                if right_idx >= 0 and left_idx <= right_idx:
                    heapq.heappush(right_heap,costs[right_idx])
                    right_idx -= 1
        
        return cost

        
