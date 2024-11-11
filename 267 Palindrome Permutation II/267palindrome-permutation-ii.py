class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        counter = Counter(s)
        # check if can be palindrome
        one_even = False
        middle = ""
        for i in counter:
            if counter[i] % 2 != 0:
                if not one_even:
                    one_even = True
                    middle = i
                else:
                    return []

        # del counter[middle]
        counter[middle] -= 1

        for i in counter:
            counter[i] //= 2

        if middle == "":
            new_s_len = len(s) // 2
            
        else:
            new_s_len = ((len(s) - 1) // 2)
            

        res = []
        def permute(substring, counter):
            if len(substring) == new_s_len:
                res.append(substring)
                return
            
            for char in counter:
                if counter[char] > 0:
                    # print(char)
                    substring += char
                    counter[char] -= 1

                    permute(substring, counter)

                    # backtrack
                    substring = substring[:-1]
                    counter[char] += 1
            
        permute("", counter)
        
        for i in range(len(res)):
            res[i] = res[i] + middle + res[i][::-1]
        return res

        

        
            
                
            
            

        
        