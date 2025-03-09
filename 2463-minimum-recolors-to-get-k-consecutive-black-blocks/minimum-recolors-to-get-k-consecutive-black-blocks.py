class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        min_whites = blocks[:k].count('W')
        window_count = min_whites
        if n == k:
            return min_whites
        for i in range(k, n):
            if blocks[i-k] == 'W':
                window_count -= 1
            if blocks[i] == 'W':
                window_count += 1
            min_whites = min(min_whites, window_count)
        return min_whites