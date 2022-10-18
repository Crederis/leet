class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        even = [x for x in nums if x % 2 == 0]
        odd = [x for x in nums if x not in even]
        j = 0
        
        for i in range(0, len(nums), 2):
            nums[i] = even[j]
            nums[i+1] = odd[j]
            j+=1
                
        return nums