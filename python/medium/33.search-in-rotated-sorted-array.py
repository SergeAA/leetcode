import enum
from typing import List
from utils import testtime

# @lc code=start


class Solution:
    # @testtime(1000)
    def search_mini(self, nums: List[int], target: int) -> int:
        return -1 if target not in nums else nums.index(target)

    def search(self, nums: List[int], target: int) -> int:
        hi = len(nums) - 1
        lo = 0

        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] == target:
                return mid
            if nums[lo] <= nums[mid]:
                if target in range(nums[lo], nums[mid] + 1):
                    hi = mid - 1
                else:
                    lo = mid + 1
            else:
                if target in range(nums[mid], nums[hi] + 1):
                    lo = mid + 1
                else:
                    hi = mid - 1
        return -1


# @lc code=end


def test(er, *args):
    ar = Solution().search(*args)
    print(f"ER: {er}\nAR: {ar}" if ar != er else "Passed", "\n")


test(4, [4, 5, 6, 7, 0, 1, 2], 0)
test(-1, [4, 5, 6, 7, 0, 1, 2], 3)
test(-1, [1], 0)
test(0, [4, 5, 6, 7, 0, 1, 2], 4)
