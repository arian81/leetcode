class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:

        banned = set(banned)

        curr_sum = 0
        count = 0
        for i in range(1, n+1):
            if i not in banned:
                if curr_sum + i <= maxSum :
                    curr_sum += i
                    count +=1
                else:
                    break
        return count
        

        