class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        k = len(flowerbed)
        for i in range(k):
            if flowerbed[i] != 0:
                continue
            
            left =  i == 0 or flowerbed[i-1] == 0
            right = i == k - 1 or flowerbed[i+1] == 0
            
            if left and right and flowerbed[i] == 0:
                flowerbed[i] = 1
                n -= 1

        return  n <= 0
            
