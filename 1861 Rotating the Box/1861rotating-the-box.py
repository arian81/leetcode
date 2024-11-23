class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:


        for i in range(len(box)):
            for j in range(1, len(box[i])):
                k = j - 1
                while k >= 0 and box[i][k + 1] == "." and box[i][k] != "*":
                    box[i][k + 1], box[i][k] = box[i][k], box[i][k+1]
                    k -= 1
                
        print(*box, sep="\n")
        new_box = [[0 for _ in range(len(box))] for _ in range(len(box[0]))]

        #rotate 90 degrees
        for i in range(len(box)):
            for j in range(len(box[i])):
                new_box[j][len(box)- 1 - i] = box[i][j]

        return new_box


        