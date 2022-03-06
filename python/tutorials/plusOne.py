from utils import List, test

# @lc code=start


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rest, res = 1, []
        for el in reversed(digits):
            nl = el + rest
            rest, nl = nl // 10, nl % 10
            res.append(nl)
        if rest:
            res.append(rest)
        return list(reversed(res))


# @lc code=end
f = Solution().plusOne

test([1], f, [0])
test([1, 2, 4], f, [1, 2, 3])
test([4, 3, 2, 2], f, [4, 3, 2, 1])
test([1, 0], f, [9])
test([9, 0, 0, 0, 0, 0, 0, 0], f, [8, 9, 9, 9, 9, 9, 9, 9])
