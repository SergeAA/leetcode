from utils import List

# @lc code=start


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        for i in range(0, len(nums)):
            if target <= nums[i]:
                return i
        return i + 1


# @lc code=end

assert Solution().searchInsert([1, 3, 5, 6], 5) == 2
assert Solution().searchInsert([1, 3, 5, 6], 2) == 1
assert Solution().searchInsert([1, 3, 5, 6], 7) == 4
assert Solution().searchInsert([], 7) == 0
