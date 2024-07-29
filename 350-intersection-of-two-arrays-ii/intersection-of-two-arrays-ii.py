class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freq = {}
        for num in nums1:
            freq[num] = freq.get(num, 0) + 1
        
        result = []
        for num in nums2:
            if freq.get(num):
                result.append(num)
                freq[num] -= 1

        return result