class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        current_index = 0
        counter = 0
        res = []
        
        for i in range(len(nums)):
            current_index = i
            for j in range(len(nums)):
                if i == j:
                    continue
                elif nums[i] > nums[j]:
                    counter += 1
                
            res.append(counter)
            counter = 0
            
        return res
                