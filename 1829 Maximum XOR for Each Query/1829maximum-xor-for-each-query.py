class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        presum = [nums[0]]
        for i in range(1,len(nums)):
            presum.append(nums[i] ^ presum[i-1])
        res = []
        for i in presum:
            # curr_max = (-1,0)
            # for k in range(2**maximumBit):
            #     calc = i ^ k
            #     if calc > curr_max[1]:
            #         curr_max = (k, calc)

            res.append(i ^ (2 ** maximumBit - 1))
        return list(reversed(res))
            
        