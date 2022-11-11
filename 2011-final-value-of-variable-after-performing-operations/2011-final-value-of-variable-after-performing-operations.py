class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        a = operations.count("X++") + operations.count("++X")
        b = operations.count("X--") + operations.count("--X")
        
        return a-b