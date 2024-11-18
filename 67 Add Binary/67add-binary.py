class Solution:
    def addBinary(self, a: str, b: str) -> str:
        res = ""
        remainder = "0"

        if len(b) < len(a):
            a, b = b, a
        
        diff = len(b) - len(a)
        a = "0" * diff + a

        print(a, b)
        
        for i in reversed(range(len(a))):
            if a[i] == "1" and b[i] == "1":
                if remainder == "1":
                    res = "1" + res
                else:
                    res = "0" + res
                    remainder = "1"
            elif a[i] == "0" and b[i] == "0":
                res = remainder + res
                remainder = "0"
            else:
                if remainder == "1":
                    res = "0" +res
                else:
                    res = "1" + res
        if remainder == "1":
            res = remainder + res
        return res

            
            

        