#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        wrd, mx = '', 0
        for i in s:
            if i in wrd:
                mx = max(len(wrd), mx)
                wrd = wrd[wrd.index(i)+1:] + i
            else:
                wrd += i
        return max(len(wrd), mx)

# @lc code=end
