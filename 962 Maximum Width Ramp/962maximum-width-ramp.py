class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        reverse_greater = [0]*len(nums)
        reverse_greater[-1] = nums[-1]
        for i in range(len(nums)-2, -1, -1):
            reverse_greater[i] = max(reverse_greater[i+1], nums[i])
        
        mx_diff = 0
        for i in range(len(nums)):
            l = i+1
            r = len(nums)
            while l<r:
                mid = (l+r)//2
                if nums[i]>reverse_greater[mid]:
                    r = mid
                elif nums[i]<=reverse_greater[mid]:
                    l = mid+1

            mx_diff = max(mx_diff, l-i-1)

        return mx_diff
            
