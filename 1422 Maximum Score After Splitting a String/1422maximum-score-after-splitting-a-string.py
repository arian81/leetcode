class Solution:
    def maxScore(self, s: str) -> int:

        init_left = s[0].count("0")
        init_right = s[1:].count("1")
        scores = [init_left + init_right]

        max_score = scores[-1]

        #werid prefix sum 
        for i in range(1, len(s) - 1):
            if s[i] == "0":
                scores.append(scores[-1] + 1)
            else:
                scores.append(scores[-1] - 1)
            
            max_score = max(scores[-1], max_score)
        return max_score
            




        