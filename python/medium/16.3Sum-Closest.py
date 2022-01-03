from typing import List
from utils import task15array, testtime

# @lc code=start


class Solution:
    @testtime(10)
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums, ln, res = sorted(nums), len(nums), None
        for i in range(0, ln - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            l, r, sm = i + 1, ln - 1, 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if sm == target:
                    return target
                if res is None or abs(target - sm) < abs(target - res):
                    res = sm

                if sm > target:
                    r -= 1
                elif sm < target:
                    l += 1

        return res


# @lc code=end

# t = [-1, 0, 1, 2, -1, -4, -1, 0, 1, 2, -1, -4, -1, 0, 1, 2, -1, -4, -1, 0, 1]

# print(Solution().threeSumClosest([-1, 2, 1, -4], 1))
# print(Solution().threeSumClosest([0, 0, 0], 1))
print(Solution().threeSumClosest([1, 1, -1, -1, 3], -1))
