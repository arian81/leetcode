class Solution:
    def findMin(self, nums: List[int]) -> int:

        lp, rp = 0, len(nums) - 1
        minValue = 100000
        while (lp <= rp):
            mid = (lp + rp) // 2
            minValue = min(nums[mid], minValue)
            if (nums[lp] < nums[rp]):
                return min(minValue, nums[lp])
            if (nums[mid] >= nums[lp]):
                lp = mid + 1
            else:
                rp = mid - 1
        return minValue 
            
        