class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivots = []
        greater = []
        smaller = []

        for num in nums:
            if num > pivot:
                greater.append(num)
            elif num == pivot:
                pivots.append(num)
            else:
                smaller.append(num)
        return smaller + pivots + greater
        