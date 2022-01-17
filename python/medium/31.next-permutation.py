import enum
from typing import List
from utils import testtime

# @lc code=start


class Solution:
    # @testtime(1000)
    def nextPermutation(self, nums: List[int]) -> None:
        ln, i = len(nums), 0
        while i < ln - 1 and nums[i] <= nums[i + 1]:
            i += 1

        if not i:
            nums.sort()
        elif i == ln - 1:
            nums[i - 1], nums[i] = nums[i], nums[i - 1]
        else:
            mx, r = nums[i], i
            for k, v in enumerate(nums[i:]):
                if mx >= v >= nums[i - 1]:
                    r, mx = k, v
            nums[i - 1], nums[i + r] = nums[i + r], nums[i - 1]
            nums[i:] = sorted(nums[i:])


# @lc code=end


def test(res, result):
    Solution().nextPermutation(res)
    print(f"ER: {result}\nAR: {res}" if res != result else "Passed", "\n")


test([2, 1, 3], [2, 3, 1])

# test([0, 1, 2, 5, 3, 3, 0], [0, 1, 3, 0, 2, 3, 5])
# test([1, 3, 2], [2, 1, 3])
# test([1, 2, 3], [1, 3, 2])
# test([3, 2, 1], [1, 2, 3])
# test([1, 1, 5], [1, 5, 1])
# test([], [])
# test([1], [1])
