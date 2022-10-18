class Solution:
    def reverseWords(self, s: str) -> str:
        s_split = s.split()
        temp = [x[::-1] for x in s_split]
        return " ".join(temp)