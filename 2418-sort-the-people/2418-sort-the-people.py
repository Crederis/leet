class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        res = []
        
        for i in heights:
            x = heights.index(max(heights))
            res.append(names[x])
            heights[x] = 0
            
        return res