class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_row_values = [min(row) for row in matrix]
        min_row_positions = {i: row.index(min(row)) for i, row in enumerate(matrix)}
        max_col_values = [max(col) for col in zip(*matrix)]

        lucky_numbers = []

        for i, min_value in enumerate(min_row_values):
            column_index = min_row_positions[i]
            if min_value == max_col_values[column_index]:
                lucky_numbers.append(min_value)
    
        return lucky_numbers
                
