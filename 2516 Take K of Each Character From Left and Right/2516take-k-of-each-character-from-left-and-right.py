class Solution:
    def isValid(self, counter, k):
        for i in ["a", "b", "c"]:
            if counter[i] < k:
                return False
        return True
    def takeCharacters(self, s: str, k: int) -> int:
        counter = Counter(s)
        
        for i in ["a", "b", "c"]: # check if possible
            if counter[i] < k:
                return -1
        
        lp = rp = 0
        curr_counts = {"a": 0, "b": 0, "c": 0}
        max_len = 0
        while rp < len(s):
            
            curr_counts[s[rp]] += 1
            if self.isValid(counter - Counter(curr_counts), k):
                max_len = max(max_len, rp - lp + 1)
            else:
                while (lp <= rp and not self.isValid(counter - Counter(curr_counts), k)):
                    curr_counts[s[lp]] -= 1
                    lp += 1
            rp += 1  
        return len(s) - max_len

            

        


        