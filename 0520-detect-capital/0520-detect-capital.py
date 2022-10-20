class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        checker = 0
        isFirst = False
        
        for i in word:
            if ord(i) in range(65, 91):
                if word.index(i) == 0:
                    isFirst = True
                else:
                    isFirst = False
                checker += 1
                
        if checker == len(word) or (checker == 1 and isFirst == True) or checker == 0:
            return True
        else:
            return False