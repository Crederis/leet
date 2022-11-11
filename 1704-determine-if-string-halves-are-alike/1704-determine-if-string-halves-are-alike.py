class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowel = ['a', 'i', 'u', 'e', 'o']
        s = s.lower()
        a = s[0 : len(s)//2]
        b = s[len(s)//2 : len(s)]
        
        x = [x for x in a if x in vowel]
        y = [y for y in b if y in vowel]
        
        if len(x) == len(y):return True
        else: return False