class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start = [0, 0]
        
        for i in moves:
            if i.lower() == "r":
                start[0] += 1
            elif i.lower() == "l":
                start[0] -= 1
            elif i.lower() == "u":
                start[1] += 1
            elif i.lower() == "d":
                start[1] -= 1
                
        if start == [0, 0]:
            return True
        else:
            return False