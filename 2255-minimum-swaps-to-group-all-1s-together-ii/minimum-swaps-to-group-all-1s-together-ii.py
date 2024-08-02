class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        total, n = sum(nums), len(nums)
        nums += nums[:total]
        onesInWindows = nums[:total].count(1)
        minSwaps = total - onesInWindows
        for i in range(1, n):
            if nums[i-1] == 1:
                onesInWindows -= 1
            if nums[i+total-1] == 1:
                onesInWindows += 1
            swaps = total - onesInWindows
            if swaps < minSwaps:
                minSwaps = swaps
        
        return minSwaps
        