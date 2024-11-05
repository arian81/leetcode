class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        sentences = sentence.split(" ")
        for i in range(len(sentences)-1):
            print(sentences[i][-1], )
            if sentences[i][-1] != sentences[i+1][0]:
                return False
        if sentences[-1][-1] != sentences[0][0]:
            return False
        return True
        