from typing import List
from utils import testtime

# @lc code=start


class Solution:
    # @testtime(1000)
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi, lr, hr = 0, len(nums) - 1, -1, -1
        if hi < 0 or nums[hi] < target or target < nums[lo]:
            return [lr, hr]

        mid = (lo + hi) // 2
        while lo <= hi and (lr < 0 or hr < 0):
            if nums[lo] == target and lr < 0:
                lr = lo
            if nums[hi] == target and hr < 0:
                hr = hi

            if nums[mid] == target:
                if lr < 0:
                    mid = (lo + mid) // 2
                    lo += 1
                    continue
                elif hr < 0:
                    mid = (hi + mid) // 2
                    hi -= 1
                    continue

            if nums[mid] > target:
                hi = mid - 1
            elif nums[mid] < target:
                lo = mid + 1

            mid = (lo + hi) // 2

        return [lr, hr]


# @lc code=end


def test(er, *args):
    ar = Solution().searchRange(*args)
    print(f"ER: {er}\nAR: {ar}" if ar != er else "Passed", "\n")


test([1, 1], [1, 4], 4)

test([0, 0], [1, 2], 1)
test([0, 1], [1, 1, 2], 1)

k = 10000
test([1, k], [1] + [2] * k + [3], 2)

test([-1, -1], [5, 7, 7, 8, 8, 10], 6)
test([3, 4], [5, 7, 7, 8, 8, 10], 8)
test([0, 2], [1, 1, 1, 4, 5, 7, 7, 7], 1)
test([5, 7], [1, 2, 3, 4, 5, 7, 7, 7], 7)
test([-1, -1], [1, 2, 3, 4, 5], 6)
test([-1, -1], [1], 0)
test([-1, -1], [], 0)
