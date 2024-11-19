class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        lp = 0
        rp = 0
        max_sum = float("-inf")
        curr_sum = 0
        while rp < len(nums):
            
            curr_sum += nums[rp]

            if nums[rp] > curr_sum:
                print(lp, rp)
                curr_sum = nums[rp]
                lp = rp
            
            max_sum = max(max_sum, curr_sum)
            rp += 1
        return max_sum


        