#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start


class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = len(s)
        for r in range(l, 0, -1):
            for i in range(0, l-r+1):
                if s[i:i+r] == s[i:i+r][::-1]:
                    return s[i:i+r]
        return s

# @lc code=end
