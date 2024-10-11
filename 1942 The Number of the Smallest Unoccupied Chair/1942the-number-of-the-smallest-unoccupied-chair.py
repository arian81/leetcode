import heapq

class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        # 0 0 0
        # time leaving array, key and list
        # occupied array
        # sort times (with added friend field)
        # with the leaving time
        # min priority queue with all elements initially there
        # have arrival? Use global min value
        # when leaving, add that unoccupied index to priority queue
        arrival_times = {x[0]: (x[1], i) for i, x in enumerate(times)}
        chairs = list(range(len(times)))
        leaving_time_chair = dict()
        time = 0

        while True:
            if time in leaving_time_chair:
                for chair in leaving_time_chair[time]:
                    heapq.heappush(chairs, chair)
                leaving_time_chair[time].clear()
            if time not in arrival_times:
                time += 1
                continue

            if arrival_times[time][1] == targetFriend:
                return heapq.heappop(chairs)

            leaving_time = arrival_times[time][0]
            if leaving_time not in leaving_time_chair:
                leaving_time_chair[leaving_time] = []
            unoccupied_chair = heapq.heappop(chairs)
            leaving_time_chair[leaving_time].append(unoccupied_chair)
            
            time += 1

        raise Error("Unreachable")

