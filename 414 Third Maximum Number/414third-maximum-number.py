class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)

        nums = [-x for x in nums]
        heapq.heapify(nums)
        
        heapq.heappop(nums)
        heapq.heappop(nums)
        return -heapq.heappop(nums)
        