class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        num_invalid = 0
        num_opening = 0
        for c in s:
            if c == "(":
                num_opening += 1
            if c == ")":
                if num_opening == 0:
                    num_invalid += 1
                else:
                    num_opening -= 1

        num_invalid += num_opening

        return num_invalid