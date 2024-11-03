# from math import ceil
# class Solution:
#     # def canEat(self, piles, speed, h):
#     #     time_taken = 0
#     #     if speed == 0:
#     #         return False
#     #     for i in piles:
#     #         time_taken += ceil(i / speed)
#     #         print(speed, time_taken, i)
#     #         if time_taken > h: #too slow
#     #             return False
#     #     return True
        
#     # def minEatingSpeed(self, piles: List[int], h: int) -> int:
#     #     lp, rp = 1, max(piles)

#     #     while (lp < rp):
#     #         mid = (lp + rp) // 2
            
#     #         time_taken = 0
#     #         for i in piles:
#     #             time_taken += ceil(i / mid)
            
#     #         if time_taken <= h:
#     #             rp = mid
#     #         else:
#     #             lp = mid + 1
#     #     return rp
    

from math import ceil
class Solution:
    def canEat(self, piles, speed, h):
        time_taken = 0
        for i in piles:
            time_taken += ceil(i / speed)
            if time_taken > h:  # too slow
                return False
        return True
        
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lp, rp = 1, max(piles)
        
        while lp <= rp:
            mid = (lp + rp) // 2
            if self.canEat(piles, mid, h):
                # If we can eat at this speed, try a lower speed
                rp = mid - 1
            else:
                # If we can't eat at this speed, try a higher speed
                lp = mid + 1
                
        return lp
