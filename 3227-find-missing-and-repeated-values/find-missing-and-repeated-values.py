class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        arr = [0] * pow(n, 2)

        for i in range(n):
            for j in range(n):
                arr[grid[i][j] - 1] += 1
        
        missing = None
        repeat = None
        for i, val in enumerate(arr):
            if val == 0:
                missing = i+1
            if val > 1:
                repeat = i+1
        
        return [repeat, missing]

