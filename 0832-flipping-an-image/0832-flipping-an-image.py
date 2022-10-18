class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        reverse_each = [x[::-1] for x in image]
        
        for i in reverse_each:
            for j in range(0, len(i)):
                if i[j] == 0:
                    i[j] = 1
                elif i[j] == 1:
                    i[j] = 0
                    
        return reverse_each