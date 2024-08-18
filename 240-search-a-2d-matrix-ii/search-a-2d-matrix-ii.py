class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        
        m = 0
        n = columns-1
        while m < rows and n >= 0:
            current = matrix[m][n]
            if current == target:
                return True
            elif current > target:
                n -= 1
            else:
                m += 1
        
        return False
