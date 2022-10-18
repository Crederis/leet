class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        even = [nums[x] for x in range(0, len(nums)) if x % 2 == 0]
        even.sort()
        odd = [nums[x] for x in range(0, len(nums)) if x % 2 != 0]
        odd.sort(reverse=True)
        temp = []
        
        for i in range(0, len(nums)):
            if i % 2 == 0:
                temp.append(even[0])
                even.pop(0)
            else:
                temp.append(odd[0])
                odd.pop(0)
                
        return temp