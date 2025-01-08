class Solution:

    def helper(self, word1, word2):
        # if len(word2) > len(word1):
        #     word1, word2 = word2, word1
        #word1 is longer word
        window = len(word1)
        # print(word1[:window], word1[-window:], word2)
        return word2[:window] == word2[-window:] == word1

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if self.helper(words[i], words[j]):
                    count += 1
        return count

        