class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        extraCandiesPreCompute = []
        maxVal = 0

        for candy in candies:
            maxVal = max(maxVal, candy)
            extraCandiesPreCompute.append(candy + extraCandies)
        
        results = []
        for candy in extraCandiesPreCompute:
            results.append(True if candy>=maxVal else False)
        
        return results