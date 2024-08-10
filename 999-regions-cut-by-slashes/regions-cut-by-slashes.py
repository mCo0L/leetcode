class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        # Create a Union-Find data structure for 4 * n * n elements
        parent = list(range(4 * n * n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        for i in range(n):
            for j in range(n):
                root = 4 * (i * n + j)
                val = grid[i][j]
                
                # Connect the parts within the cell
                if val in '/ ':
                    union(root + 0, root + 3)
                    union(root + 1, root + 2)
                if val in '\\ ':
                    union(root + 0, root + 1)
                    union(root + 2, root + 3)
                
                # Connect to the right cell
                if j + 1 < n:
                    union(root + 1, root + 7)
                # Connect to the cell below
                if i + 1 < n:
                    union(root + 2, root + 4 * n)
        
        # Count the number of distinct regions
        return sum(find(x) == x for x in range(4 * n * n))