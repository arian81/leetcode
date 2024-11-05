class Solution:
    def minChanges(self, s: str) -> int:
        return sum(s[ptr] != s[ptr+1] for ptr in range(0, len(s), 2))
        