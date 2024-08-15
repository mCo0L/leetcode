class Solution:
    def canBeChunked(self, arr, i, j):
        count = 0
        for index in range(i,j+1):
            if arr[index] >= i and arr[index] <= j:
                print(arr[index])
                count += 1
        
        if count == j-i+1:
            return True
        return False

    def maxChunksToSorted(self, arr: List[int]) -> int:
        n = len(arr)
        chunks = 0

        i = 0
        while i < n:
            j = i
            for j in range(i, n):               
                if self.canBeChunked(arr, i, j):
                    print(f'{i} {j} - can break')
                    break
            chunks += 1
            i = j+1
        return chunks
            