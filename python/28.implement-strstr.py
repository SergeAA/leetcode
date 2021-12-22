# @lc code=start


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        ln = len(needle)
        if not ln:
            return 0
        for i in range(0, len(haystack) - ln + 1):
            if haystack[i : i + ln] == needle:
                return i
        return -1


# @lc code=end

assert Solution().strStr("hello", "ll") == 2
assert Solution().strStr("had asdsad saello", "ad") == 1
assert Solution().strStr("", "ll") == -1
assert Solution().strStr("hello", "") == 0
