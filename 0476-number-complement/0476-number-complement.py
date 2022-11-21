class Solution:
    def findComplement(self, num: int) -> int:
        binary = [x for x in str(bin(num))[2:]]
        res = 0
        
        for i in range(len(binary)):
            if binary[i] == "0":
                binary[i] = "1"
            else:
                binary[i] = "0"
                
        a = "".join(binary)
        
        for i in a:
            res = res * 2 + int(i)
            
        return res