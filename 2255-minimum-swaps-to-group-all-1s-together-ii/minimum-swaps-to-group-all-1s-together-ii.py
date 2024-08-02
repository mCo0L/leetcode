class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        ones, n = sum(nums), len(nums)
        nums += nums[:ones]
        onesInWindow = nums[:ones].count(1)
        minSwaps = ones - onesInWindow
        for i in range(1, n):
            if nums[i-1] == 1:
                onesInWindow -= 1
            if nums[i+ones-1] == 1:
                onesInWindow += 1
            swaps = ones - onesInWindow
            if swaps < minSwaps:
                minSwaps = swaps
        
        return minSwaps
        