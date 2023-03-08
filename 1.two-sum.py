#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            required_num = target - num
            for inner_index, inner_num in enumerate(nums[index+1:]):
                if inner_num == required_num:
                    return index, index+inner_index+1

# @lc code=end
