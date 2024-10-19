def invert(string):
    new_str = ""
    for i in string:
        if i == "0":
            new_str  += "1"
        else:
            new_str += "0"
    return new_str

def get_string(n):
    if n == 1:
            return "0"
    else:
        return get_string(n-1) + "1" + invert(get_string(n-1))[::-1]

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return get_string(n)[k-1]
        
        