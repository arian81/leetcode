class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix_sum = []
        vowels = set(["a", "e", "i","o", "u"])
        count = 0
        for i in words: 
            if i[0] in vowels and i[-1] in vowels:
                count += 1
            prefix_sum.append(count)
        
        res = []
        for start, end in queries:
            if start == 0:
                res.append(prefix_sum[end])
            else:
                res.append(prefix_sum[end] - prefix_sum[start-1])

        return res


        