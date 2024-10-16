class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        buff = {}
        for idx, num in enumerate(nums):
            diff = target - num 
            if diff in buff:
                return [idx, buff[diff]]
            else:
                buff[num] = idx
