class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s = "".join([letter for letter in s.lower() if letter.isalnum()])
        # return s == s[::-1]
        clean = ""
        for i in s:
            if i.isalnum():
                clean += i.lower()
        s = clean
        print(s)
        for i in range(len(s) // 2):
            left = s[i]
            right = s[len(s)-i - 1]
            if left != right:
                return False
        return True
            

