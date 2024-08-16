class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        maxVal = max(candies)
        results = []
        for candy in candies:
            results.append(True if candy + extraCandies >= maxVal else False)
        
        return results