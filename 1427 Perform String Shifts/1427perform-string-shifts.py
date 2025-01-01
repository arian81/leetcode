class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        for i in shift:
            dir, amount = i
            amount %= len(s)
            s = (s[-amount:] + s[:-amount]) if dir else (s[amount:] + s[:amount])
        return s
        