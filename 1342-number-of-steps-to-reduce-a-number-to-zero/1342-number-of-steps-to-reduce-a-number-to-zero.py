class Solution:
    def numberOfSteps(self, num: int) -> int:
        opt = 0
        
        while num > 0:
            if num % 2 == 0:
                num /= 2
            else:
                num -= 1
            
            opt +=1
            
        return opt