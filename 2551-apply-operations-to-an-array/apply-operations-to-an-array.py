from itertools import count
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        
        arr = [0] * n
        count = 0
        for i in range(n):
            if nums[i] != 0:
                arr[count] = nums[i]
                count += 1
        return arr

        