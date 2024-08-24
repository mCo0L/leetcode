class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        n, m = len(mat) , len(mat[0])
        prefix_sum = [[0] * m for _ in range(n)]

        # Compute the prefix sum
        for i in range(n):
            for j in range(m):
                prefix_sum[i][j] = mat[i][j]
                if i > 0:
                    prefix_sum[i][j] += prefix_sum[i - 1][j]
                if j > 0:
                    prefix_sum[i][j] += prefix_sum[i][j - 1]
                if i > 0 and j > 0:
                    prefix_sum[i][j] -= prefix_sum[i - 1][j - 1]

        result = [[0] * m for _ in range(n)]

        for i in range(n):
            for j in range(m):
                x1 = max(0, i - k)
                x2 = min(n - 1, i + k)
                y1 = max(0, j - k)
                y2 = min(m - 1, j + k)
                sum = prefix_sum[x2][y2]

                if x1 > 0:
                    sum -= prefix_sum[x1 - 1][y2]

                if y1 > 0:
                    sum -= prefix_sum[x2][y1 - 1]

                if x1 > 0 and y1 > 0:
                    sum += prefix_sum[x1 - 1][y1 - 1]

                result[i][j] = sum
        
        return result
    