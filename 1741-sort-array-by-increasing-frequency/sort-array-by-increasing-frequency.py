class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        nums.sort(key=lambda x: (frequency[x], -x))
        return nums