# @lc code=start


class Solution:
    def myAtoi(self, s: str) -> int:
        flag, sign, res = False, 1, 0

        for i in s:
            if not flag and i in [" ", "+", "-"]:
                flag = i != " "
                if i == "-":
                    sign = -1
                continue

            num = ord(i) - 48
            if 0 <= num <= 9:
                res = res * 10 + num
                flag = True
            else:
                break

        res = sign * res
        if res > 2147483647:
            res = 2147483647
        if res < -2147483648:
            res = -2147483648

        return res


# @lc code=end

print(Solution().myAtoi("    -21474836472"))
