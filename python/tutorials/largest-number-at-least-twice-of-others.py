from utils import List, test

# @lc code=start


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx, pm, ix = 0, 0, -1
        for i, el in enumerate(nums):
            if el > mx:
                pm, mx, ix = mx, el, i
            elif el > pm:
                pm = el
        return ix if pm * 2 <= mx else -1


# @lc code=end
f = Solution().dominantIndex

test(-1, f, [0, 0, 3, 2])
test(-1, f, [])
test(1, f, [3, 6, 1, 0])
test(-1, f, [1, 2, 3, 4])
test(0, f, [1])
