#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(1, 201):
            for cur in strs[1:]:
                if cur[0:i] != strs[0][0:i]:
                    return res
            res = strs[0][0:i]
        return res


# @lc code=end


a = Solution()

print(a.longestCommonPrefix(["flower"]))
print(a.longestCommonPrefix(["flower", "flow", "flight"]))
print(a.longestCommonPrefix(["dog", "racecar", "car"]))
