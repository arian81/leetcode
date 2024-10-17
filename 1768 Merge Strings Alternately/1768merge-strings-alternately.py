class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # remainder = ""
        # if len(word1) > len(word2):
        #     len_diff = len(word1) - len(word2) - 1
        #     remainder = word1[len_diff:]
        # elif len(word1) < len(word2):
        #     len_diff = len(word2) - len(word1) - 1
        #     remainder = word2[len_diff:]
        
        # return "".join([x+y for (x,y) in list(zip(word1, word2))]) + remainder

        merged = ""
        word1 = list(word1)
        word2 = list(word2)
        while len(word1) > 0 and len(word2) > 0:
            to_add = word1.pop(0) + word2.pop(0)
            merged += to_add
        return merged + "".join(word1) + "".join(word2)