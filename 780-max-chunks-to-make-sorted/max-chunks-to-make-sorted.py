class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        count = 0
        n = len(arr)
        imax = -1
       
       
        for i in range(n):
            imax = max(imax, arr[i])
            if imax == i:
                count += 1
                imax = -1
        
        return count
            