#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start


class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        i = int(s[::-1] if x >= 0 else '-'+s[1:][::-1])
        return i if abs(i) <= 2147483647 else 0

# @lc code=end
