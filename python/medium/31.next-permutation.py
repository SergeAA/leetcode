import enum
from typing import List
from utils import testtime

# @lc code=start


class Solution:
    # @testtime(1000)

    def nextPermutation(self, nums: List[int]) -> None:
        ln = len(nums)
        for i in range(ln - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pv = i
                for j in range(pv, ln):
                    if nums[j] <= nums[pv] and nums[i - 1] < nums[j]:
                        pv = j
                nums[i - 1], nums[pv] = nums[pv], nums[i - 1]
                nums[i:] = sorted(nums[i:])
                return
        nums.sort()


# @lc code=end


def test(res, result):
    Solution().nextPermutation(res)
    print(f"ER: {result}\nAR: {res}" if res != result else "Passed", "\n")


test([2, 1, 3], [2, 3, 1])

test([0, 1, 2, 5, 3, 3, 0], [0, 1, 3, 0, 2, 3, 5])
test([1, 3, 2], [2, 1, 3])
test([1, 2, 3], [1, 3, 2])
test([3, 2, 1], [1, 2, 3])
test([1, 1, 5], [1, 5, 1])
test([], [])
test([1], [1])
