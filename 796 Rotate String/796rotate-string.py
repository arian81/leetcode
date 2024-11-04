class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            rotated = s[1:] + s[0]
            s = rotated
            if rotated == goal:
                return True
        return False
        