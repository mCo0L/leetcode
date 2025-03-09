class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        if k > n:
            return -1
        min_whites = blocks[:k].count('W')
        for i in range(1, n-k+1):
            min_whites = min(min_whites, blocks[i:i+k].count('W'))
        
        return min_whites