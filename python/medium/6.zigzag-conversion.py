# @lc code=start


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = s if numRows < 2 or numRows > len(s) else ""
        row, it, step = 0, 0, 2 * numRows - 2
        while len(res) < len(s):
            res += s[it : it + 1]
            if 0 < row < numRows - 1:
                zz = it + 2 * (numRows - (row + 1))
                res += s[zz : zz + 1]
            if it + step > len(s):
                row += 1
                it = row
            else:
                it += step
        return res


# @lc code=end


s = ""
numRows = 4
r = ""
t = Solution().convert(s, numRows)
print(s, r == t, t)

s = "PAYP"
numRows = 4
r = "PAYP"
t = Solution().convert(s, numRows)
print(s, r == t, t)


s = "PAYPALISHIRING"
numRows = 4
r = "PINALSIGYAHRPI"
t = Solution().convert(s, numRows)
print(s, r == t, t)

numRows = 3
r = "PAHNAPLSIIGYIR"
t = Solution().convert(s, numRows)
print(s, r == t, t)

numRows = 5
r = "PHASIYIRPLIGAN"
t = Solution().convert(s, numRows)
print(s, r == t, t)
