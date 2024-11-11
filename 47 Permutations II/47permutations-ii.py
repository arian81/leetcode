class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []


        def dfs(subset, counter):
            if len(subset) == len(nums):
                res.append(subset.copy())
                return
            
            for num in counter:
                if counter[num] > 0:
                    subset.append(num)
                    counter[num] -= 1
                    dfs(subset, counter)

                    subset.pop()
                    counter[num] += 1
        dfs([], Counter(nums))
        return res
