class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = [x ** 2 for x in nums]
        new_nums.sort()
        return new_nums