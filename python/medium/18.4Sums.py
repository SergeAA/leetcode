from typing import List
from itertools import combinations
from utils import task18, task18res, testtime

CNT = 100
# @lc code=start


class Solution:
    # @testtime(CNT)
    # def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    #     res = set()
    #     for k in combinations(nums, 4):
    #         if sum(k) == target:
    #             res.add(tuple(sorted(list(k))))
    #     return list(res)

    @testtime(CNT)
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums, ln, res = sorted(nums), len(nums), []
        for k in range(0, ln - 3):
            if k and nums[k] == nums[k - 1]:
                continue
            for i in range(k + 1, ln - 2):
                if i > k + 1 and nums[i] == nums[i - 1]:
                    continue
                l, r, sm = i + 1, ln - 1, 1
                while l < r:
                    sm = nums[i] + nums[l] + nums[r] + nums[k]
                    if sm > target:
                        r -= 1
                    elif sm < target:
                        l += 1
                    else:
                        res.append([nums[i], nums[l], nums[r], nums[k]])
                        l += 1
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
        return res


# @lc code=end

print(
    Solution().fourSum([-5, 5, 4, -3, 0, 0, 4, -2], 4),
    [[-5, 0, 4, 5], [-3, -2, 4, 5]],
)

print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
print(Solution().fourSum([2, 2, 2, 2], 8))
print(Solution().fourSum(task18, task18res))
