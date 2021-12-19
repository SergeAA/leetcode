#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start


class Solution:
    def isPalindrome(self, x: int) -> bool:
        k, s = 0, x
        while s > 0:
            k = k*10 + s % 10
            s //= 10
        return k == x

# @lc code=end
