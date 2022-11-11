class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        for word in words:
            # if list(allowed) == list(set(word)):
            if all(x in list(allowed) for x in list(set(word))):
                counter += 1
                
        return counter