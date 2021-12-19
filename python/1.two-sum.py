#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, r in enumerate(nums[:-1]):
            for j, l in enumerate(nums[i+1:]):
                if (r + l) == target:
                    return [i, j+i+1]
        return [None, None]

# @lc code=end
