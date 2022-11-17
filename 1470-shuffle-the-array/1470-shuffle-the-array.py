class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        a = len(nums) // 2
        nums1 = nums[:a]
        nums2 = nums[a:]
        res = []
        
        for i in range(a):
            res.append(nums1[i])
            res.append(nums2[i])
            
        return res