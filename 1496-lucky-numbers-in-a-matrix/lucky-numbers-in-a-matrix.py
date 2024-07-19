class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row_values = [min(row) for row in matrix]
        
        # Step 2: Identify the columns of the minimum elements
        min_row_positions = {i: row.index(min(row)) for i, row in enumerate(matrix)}
        
        lucky_numbers = []
        
        # Step 3: Check if the minimum element in the row is the maximum in its column
        for i, min_value in enumerate(min_row_values):
            column_index = min_row_positions[i]
            if all(matrix[row][column_index] <= min_value for row in range(len(matrix))):
                lucky_numbers.append(min_value)
        
        return lucky_numbers