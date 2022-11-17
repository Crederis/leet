class Solution:
    def trimMean(self, arr: List[int]) -> float:
        a = len(arr)
        b = a // 20
        arr.sort()
        # print(f"a: {a} | arr: {arr}")
        new_arr = arr[b:a-b]
        return sum(new_arr) / len(new_arr)