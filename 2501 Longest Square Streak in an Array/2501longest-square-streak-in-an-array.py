class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = -1
        for i in nums:
            curr_long = 0
            val = i
            for j in range(5):
                if val in numSet:
                    print(val)
                    curr_long+=1
                    val = val ** 2
            if curr_long > 1:     
                longest = max(longest, curr_long)
        return longest

        