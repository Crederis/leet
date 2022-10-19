class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        a = [int(x) for x in str(n)]
        b = sum(a)
        c = 1
        
        for i in a:
            c*=i
            
        return (c-b)
        