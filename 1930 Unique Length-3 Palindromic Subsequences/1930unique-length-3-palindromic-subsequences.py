class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        return sum([len(set(s[s.index(x) + 1:s.rindex(x)])) for x in set(s)])
            






        