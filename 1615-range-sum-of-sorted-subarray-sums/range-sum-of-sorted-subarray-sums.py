class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        all_subarrrays = []

        for i in range(n):
            sub_sum = 0
            for j in range(i, n):
                sub_sum += nums[j]
                all_subarrrays.append(sub_sum)
        all_subarrrays.sort()
        return sum(all_subarrrays[left-1:right]) % 1000000007