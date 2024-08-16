class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = len(flowerbed)
        count = 0
        for i in range(k):
            if flowerbed[i] != 0:
                continue
            
            left = 0
            if i > 0:
                left += flowerbed[i-1]
            right = 0
            if i < k - 1:
                right += flowerbed[i+1]
            
            if left + right == 0:
                flowerbed[i] = 1
                count += 1
            

        return True if count >= n else False
            
