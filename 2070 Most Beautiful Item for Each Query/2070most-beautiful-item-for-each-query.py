class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        items.sort(key=lambda item: (item[0], item[1]))

        maxB = items[0][1]
        for i in range(len(items)):
            maxB = max(maxB, items[i][1])
            items[i][1] = maxB 
        print(items)
        
        res = []
        for i in queries:
            lp, rp = 0, len(items) - 1
            maxB = 0
            while(lp <= rp):
                mid = (lp + rp) // 2

                price, beauty = items[mid]
                
                if price > i:
                    rp = mid - 1
                else:
                    maxB = max(maxB, beauty)
                    lp = mid + 1
            res.append(maxB)
        return res
        



        