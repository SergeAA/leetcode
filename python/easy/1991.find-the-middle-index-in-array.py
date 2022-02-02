from utils import List, test

# @lc code=start


class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        ls, rs, i = 0, sum(nums), -1
        for key, num in enumerate(nums):
            if ls == rs - num:
                return key
            rs = rs - num
            ls += num
        return i


# @lc code=end
f = Solution().findMiddleIndex

test(-1, f, [])
test(3, f, [2, 3, -1, 8, 4])
test(2, f, [1, -1, 4])
test(-1, f, [2, 5])
test(3, f, [1, 7, 3, 6, 5, 6])
test(-1, f, [1, 2, 3])
test(0, f, [2, 1, -1])
