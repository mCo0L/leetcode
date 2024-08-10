class Solution:
    def is_magic_square(self, grid, x, y):
        num_hash = {}
        for i in range(x, x+3):
            for j in range(y, y+3):
                if grid[i][j] < 1 or grid[i][j] > 9 or num_hash.get(grid[i][j]):
                    return False
                num_hash[grid[i][j]] = 1
        
        rsum = grid[x][y] + grid[x+1][y+1] + grid[x+2][y+2]
        
        # Diagnol
        if  rsum != grid[x][y+2] + grid[x+1][y+1] + grid[x+2][y]:
            return False
        
        
        for i in range(3):
            row_sum = grid[x+i][y] + grid[x+i][y+1] + grid[x+i][y+2]
            col_sum = grid[x][y+i] + grid[x+1][y+i] + grid[x+2][y+i]
            
            if row_sum != rsum:
                return False
            
            if col_sum != rsum:
                return False
            
        return True

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        if rows < 3 or cols <3:
            return 0
        
        magic_squares = 0
        for i in range(rows-2):
            for j in range(cols-2):
                if self.is_magic_square(grid, i, j):
                    magic_squares += 1
        
        return magic_squares