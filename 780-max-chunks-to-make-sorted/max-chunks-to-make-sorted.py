class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        prevMax = -1
        count = 0
        n = len(arr)
        for i in range(n):
            prevMax = max(prevMax, arr[i])
            if i == prevMax:
                count += 1
        
        return count
            