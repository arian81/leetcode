class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)

        res = 0
        curr_sum = 0
        nums.pop(-1)
        for i in nums:
            curr_sum += i
            print(i, curr_sum, total_sum - curr_sum) 
            if total_sum - curr_sum <= curr_sum:
                res+=1
        return res