class Solution:
    def canSwap(self, num1, num2):
        print(bin(num1), bin(num2))
        return bin(num1).count("1") == bin(num2).count("1")

    def canSortArray(self, nums: List[int]) -> bool:
        for i in range(1, len(nums)):
            ptr = i - 1 
            while(ptr >= 0 and nums[ptr+1] < nums[ptr]):
                if self.canSwap(nums[ptr + 1], nums[ptr]):
                    print(nums[ptr + 1], nums[ptr])
                    nums[ptr + 1], nums[ptr] = nums[ptr], nums[ptr+1]
                else:
                    return False
                ptr -= 1
        return True
        