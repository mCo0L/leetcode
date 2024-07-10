class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positiveNums = list()
        negativeNums = list()
        newArr = list()
        for num in nums:
            if num < 0:
                negativeNums.append(num)
            else:
                positiveNums.append(num)
        
        positiveIndex = 0
        negativeIndex = 0

        for i in range(len(nums)):
            if i%2==0:
                newArr.append(positiveNums[positiveIndex])
                positiveIndex += 1
            else:
                newArr.append(negativeNums[negativeIndex])
                negativeIndex += 1

        return newArr