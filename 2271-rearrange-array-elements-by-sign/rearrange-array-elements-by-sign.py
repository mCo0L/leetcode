class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positiveNums = list()
        negativeNums = list()

        # Separate positive and negative numbers
        for num in nums: 
            if num < 0:
                negativeNums.append(num)
            else:
                positiveNums.append(num)

        return itertools.chain(*zip(positiveNums, negativeNums))