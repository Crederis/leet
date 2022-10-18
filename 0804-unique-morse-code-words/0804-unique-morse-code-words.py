class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alp = {
            "a": ".-",
            "b": "-...",
            "c": "-.-.",
            "d": "-..",
            "e": ".",
            "f": "..-.",
            "g": "--.",
            "h": "....",
            "i": "..",
            "j": ".---",
            "k": "-.-",
            "l": ".-..",
            "m": "--",
            "n": "-.",
            "o": "---",
            "p": ".--.",
            "q": "--.-",
            "r": ".-.",
            "s": "...",
            "t": "-",
            "u": "..-",
            "v": "...-",
            "w": ".--",
            "x": "-..-",
            "y": "-.--",
            "z":"--.."
        }
        
        temp = []
        
        for i in words:
            s = ""
            for j in i:
                s += alp.get(j)
            temp.append(s)
            
        return len(set(temp))
                