class FirstUnique:

    def __init__(self, nums: List[int]):
        self.q = nums
        self.counts = {}

        for i in nums:
            if i in self.counts:
                self.counts[i] += 1
            else:
                self.counts[i] = 1
        
        

    def showFirstUnique(self) -> int:
        for i in self.q:
            if self.counts[i] == 1:
                return i
        return -1
        

    def add(self, value: int) -> None:
        self.q.append(value)
        if value in self.counts:
            self.counts[value] += 1
        else:
            self.counts[value] = 1
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)