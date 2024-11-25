class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        lst = set()
        for i in nums:
            if i in lst:
                return True
            else:
                lst.add(i)
        return False