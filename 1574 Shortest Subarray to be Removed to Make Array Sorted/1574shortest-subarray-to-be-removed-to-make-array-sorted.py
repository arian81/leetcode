class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:

        if len(arr) < 2:
            return 0
        lp, rp = 0, len(arr) - 1

        while rp > 0:
            if arr[rp - 1] > arr[rp]:
                break
            rp -= 1
    
        while lp < len(arr) - 1:
            if arr[lp + 1] < arr[lp]:
                break
            lp += 1
        
        if lp == len(arr) - 1:
            return 0
        
        ans = min(rp, len(arr) - lp - 1)  # length of middle portion
            
            # Try keeping left portion and different amounts of right portion
        i = 0
        j = rp
        while i <= lp and j < len(arr):
            if arr[i] <= arr[j]:
                ans = min(ans, j - i - 1)
                i += 1
            else:
                j += 1
                
        return ans
