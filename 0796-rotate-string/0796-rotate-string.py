class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        moves = len(s)
        a = list(s)
        
        while moves > 0:
            a.insert(0, a.pop())
            if "".join(a) == goal:
                return True
            moves -= 1
            
        return False