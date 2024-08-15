class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        prevMax = -1
        count = 0
        for i in range(len(arr)):
            prevMax = max(prevMax, arr[i])
            if i == prevMax:
                count += 1
        
        return count
            