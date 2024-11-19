class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        new_start, new_end = newInterval
        res = []
        ptr = 0
        
        #no conflicts
        while (ptr < len(intervals) and new_start > intervals[ptr][1]):
            res.append(intervals[ptr])
            ptr +=1 

        #conflict have to merge, we already know new_start < curr_end
        while(ptr < len(intervals) and new_end >= intervals[ptr][0]):
            newInterval[0] = min(newInterval[0], intervals[ptr][0])
            newInterval[1] = max(newInterval[1], intervals[ptr][1])
            ptr += 1
        
        res.append(newInterval)

        while (ptr < len(intervals)):
            res.append(intervals[ptr])
            ptr+=1
        
        return res
