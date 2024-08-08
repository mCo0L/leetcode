class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        def key(yx, e=1e-9):
            y, x = yx[0] - rStart, yx[1] - cStart
            return (max(abs(x), abs(y)), (atan2(y, x) - atan2(-1, 1+e)) % (2 * pi))
        return sorted(product(range(rows), range(cols)), key=key)