class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) % 2 == 0:
            return nums[int(len(nums)/2)]
        else:
            return nums[int((len(nums)-1)/2)]