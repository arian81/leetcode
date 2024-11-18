class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s) 
        longest = 0
        found_odd = False
        for i in counter:
            if counter[i] % 2 == 0:
                longest += counter[i]
            else:
                if found_odd:
                    longest += counter[i] - 1
                else:
                    longest += counter[i]
                    found_odd = True
            print(i, counter[i], longest)
        
        return int(longest)