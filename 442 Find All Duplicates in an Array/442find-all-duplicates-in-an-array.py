class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = {}
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        res_really = []
        for key,value in res.items():
            if value == 2:
                res_really.append(key)

        return res_really
        