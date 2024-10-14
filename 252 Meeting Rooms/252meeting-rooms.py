def collide(interval1, interval2):
    if interval1[0] < interval2[0] < interval1[1]:
        return True
    if interval2[0] < interval1[0] < interval2[1]:
        return True
    if interval1 == interval2:
        return True
    return False

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda interval: interval[0])
        print(sorted_intervals)
        for i in range(0,len(sorted_intervals)-1):
            if collide(sorted_intervals[i], sorted_intervals[i+1]):
                return False
        return True
        