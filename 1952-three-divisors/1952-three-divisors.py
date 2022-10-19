class Solution:
    def isThree(self, n: int) -> bool:
        if n <= 3:
            return False
        else:
            res = []
            for i in range(1, n+1):
                if n % i == 0:
                    res.append(i)
            
            if len(res) == 3:
                return True
            else:
                return False