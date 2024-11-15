class Solution:
    def rob(self, nums: List[int]) -> int:

        # cache = {}

        # def recurse(nums, idx, memo):
        #     if len(nums) == 0:
        #         return 0
        #     if len(nums) < 2:
        #         return max(nums)

        #     if idx in memo:
        #         return memo[idx]

        #     res = max(nums[idx] + recurse(nums[:idx-1], idx - 2, memo), recurse(nums[:idx], idx - 1, memo))
            
        #     memo[idx] = res
        #     return res 
        # return recurse(nums, len(nums) - 1, cache)

        if len(nums) == 0:
            return 0
        if len(nums) < 2:
            return max(nums)
        
        dp = [nums[0], max(nums[0], nums[1])]

        for i in range(2, len(nums)):
            dp[0], dp[1] = dp[1], max(nums[i] + dp[0], dp[1])
        
        return dp[1]