class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = Counter(nums)
        majority = 0
        majority_val = 0
        for i in c:
            if c[i] > majority_val:
                majority_val = c[i]
                majority = i
        return majority
