class Solution:
    def sortSentence(self, s: str) -> str:
        x = s.split()
        res = [""]*9
        
        for i in x:
            a = int(i[-1])
            res[a-1] = i[:-1]
            print(res)
            
        return " ".join(res).strip()