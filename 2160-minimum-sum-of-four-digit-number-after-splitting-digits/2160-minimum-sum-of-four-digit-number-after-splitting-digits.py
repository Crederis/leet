class Solution:
    def minimumSum(self, num: int) -> int:
        x = [x for x in str(num)]
        x.sort()
        return(int(x[0]+x[3]) + int(x[1]+x[2]))