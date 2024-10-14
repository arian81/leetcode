import math


class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:

        score = 0
        
        max_heap = [-i for i in nums]
        heapq.heapify(max_heap)

        for i in range(k):
            max_num = -heapq.heappop(max_heap)
            score += max_num

            heapq.heappush(max_heap, -math.ceil(max_num / 3))

        return score

        