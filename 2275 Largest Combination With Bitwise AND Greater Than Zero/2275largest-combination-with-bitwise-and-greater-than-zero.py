class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        counts = {}
        for i in candidates:
            bin_value = bin(i)[2:]
            bin_value = "0" * (24 - len(bin_value)) + bin_value
            for idx in range(len(bin_value)):
                if bin_value[idx] == "1":
                    # print(bin_value[idx])
                    if idx in counts:
                        counts[idx] += 1
                    else:
                        counts[idx] = 1
        return max(counts.values())
        