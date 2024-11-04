class Solution:
    def compressedString(self, word: str) -> str:

        comp = ""

        while(word != ""):
            current_letter = word[0]
            ptr = 0
            while(ptr < len(word) and word[ptr] == current_letter):
                ptr += 1
            buckets = ptr
            while (buckets > 0):
                if buckets > 9:
                    val = 9
                else:
                    val = buckets
                comp += f"{val}{current_letter}"
                buckets -= 9

            word = word[ptr:]
        return comp

        