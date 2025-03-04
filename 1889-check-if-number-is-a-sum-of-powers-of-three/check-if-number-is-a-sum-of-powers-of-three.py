class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        nums = []
        while n:
            n, r = divmod(n, 3)
            nums.append(str(r))
        return nums.count("2") == 0
            

        