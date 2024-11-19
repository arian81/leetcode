class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        freq = defaultdict(int)
        lp = 0
        rp = 0
        curr_sum = 0
        
        while rp < len(nums):
            curr_sum += nums[rp]
            freq[nums[rp]] += 1
            if rp - lp + 1 > k:
                curr_sum -= nums[lp]
                freq[nums[lp]] -= 1
                if freq[nums[lp]] == 0:
                    freq.pop(nums[lp])
                lp += 1
            if len(freq) == k:
                print("here")
                max_sum = max(max_sum, curr_sum)
            print(curr_sum)
            
            rp += 1
        return max_sum