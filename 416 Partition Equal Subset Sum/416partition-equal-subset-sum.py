def subset_sum(set, sum, n):
 
    # The value of subset[i][j] will be
    # true if there is a
    # subset of set[0..j-1] with sum equal to i
    subset = ([[False for i in range(sum + 1)]
            for i in range(n + 1)])
 
    # If sum is 0, then answer is true
    for i in range(n + 1):
        subset[i][0] = True
 
    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(1, sum + 1):
        subset[0][i] = False
 
    # Fill the subset table in bottom up manner
    for i in range(1, n + 1):
        for j in range(1, sum + 1):
            if j < set[i-1]:
                subset[i][j] = subset[i-1][j]
            if j >= set[i-1]:
                subset[i][j] = (subset[i-1][j] or
                                subset[i - 1][j-set[i-1]])
 
    return subset[n][sum]
class Solution:

    def canPartition(self, nums: List[int]) -> bool:
        # find a subset that equals half of the total sum of the array
        
        if (sum(nums) % 2 != 0):
            return False
        half_sum = int(sum(nums) / 2)
        

        return subset_sum(nums, half_sum, len(nums))




        
        