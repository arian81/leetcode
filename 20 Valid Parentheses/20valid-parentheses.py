class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i == "(" or i == "{" or i == "[":
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                val = stack.pop()
                if i == ")" and val != "(":
                    return False
                elif i == "}" and val != "{":
                    return False
                elif i == "]" and val != "[":
                    return False

        return len(stack) == 0

        