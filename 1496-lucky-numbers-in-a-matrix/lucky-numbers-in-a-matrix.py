class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        results = list()
        cols = len(matrix)
        for i, l in enumerate(matrix):
            for j, num in enumerate(l):
                min_row = min(l)
                max_col = num
                for k in range(cols):
                    if num < matrix[k][j]:
                        max_col = matrix[k][j]
                
                if num == min_row and num == max_col:
                    results.append(num)
        
        return results