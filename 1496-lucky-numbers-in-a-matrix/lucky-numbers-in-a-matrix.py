class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        
        # Step 1: Find the minimum element in each row
        min_row_values = [min(row) for row in matrix]
        
        # Step 2: Identify the columns of the minimum elements
        min_row_positions = {i: row.index(min(row)) for i, row in enumerate(matrix)}
        
        # Step 3: Find the maximum element in each column
        max_col_values = [max(col) for col in zip(*matrix)]
        
        lucky_numbers = []
        
        # Step 4: Check if the minimum element in the row is the maximum in its column
        for i, min_value in enumerate(min_row_values):
            column_index = min_row_positions[i]
            if min_value == max_col_values[column_index]:
                lucky_numbers.append(min_value)
        
        return lucky_numbers
                
