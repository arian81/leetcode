class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        if k == 0:
            return [0] * len(code)
        elif k < 0:
            res = []
            for i in range(len(code)):
                sum_num = 0
                for j in range(1, abs(k)+1):
                    print(i, i - j)
                    sum_num += code[(i - j) % len(code)]
                res.append(sum_num)
            return res
        else:
            res = []
            for i in range(len(code)):
                sum_num = 0
                for j in range(1,k + 1):
                    sum_num += code[(i + j) % len(code)]
                res.append(sum_num)
            return res
        