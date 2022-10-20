class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        res_a = []
        res_b = []
        
        for i in range(1, a+1):
            if a % i == 0:
                res_a.append(i)
                
        for i in range(1, b+1):
            if b % i == 0:
                res_b.append(i)
                
        return(len([x for x in res_a if x in res_b]))
            