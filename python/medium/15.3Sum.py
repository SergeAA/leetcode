from typing import List
from utils import task15array, testtime

# @lc code=start


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums, ln, res = sorted(nums), len(nums), []
        for i in range(0, ln - 2):
            if i and nums[i] == nums[i - 1]:
                continue
            l, r, sm = i + 1, ln - 1, 1
            while l < r:
                sm = nums[i] + nums[l] + nums[r]
                if sm > 0:
                    r -= 1
                elif sm < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
        return res


# @lc code=end

# t = [-1, 0, 1, 2, -1, -4, -1, 0, 1, 2, -1, -4, -1, 0, 1, 2, -1, -4, -1, 0, 1]
t = [-4, -4, -4, -1, -1, -1, -1, -1, -1, -1, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2]
t = [-4, -1, -1, 0, 1, 2]


@testtime(10)
def tst(t):
    return Solution().threeSum(t)


tst(task15array)

print(tst([0, 0, 0, 0]))
print(tst(t))

# print(Solution().threeSum(task15array))
