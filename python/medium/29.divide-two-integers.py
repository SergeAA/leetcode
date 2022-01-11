from utils import testtime


class Solution:
    @testtime(1000)
    def divide(self, dividend: int, divisor: int) -> int:
        res, ne = 0, dividend ^ divisor
        dividend, divisor = abs(dividend), abs(divisor)
        if divisor == 1:
            res = dividend
        else:
            for i in range(31, -1, -1):
                if divisor << i <= dividend:
                    dividend -= divisor << i
                    res += 1 << i

        res = -res if ne < 0 else res
        if res > (1 << 31) - 1:
            return (1 << 31) - 1
        if res < -1 << 31:
            return -1 << 31
        return res


# @lc code=end


def test(dividend, divisor, result):
    res = Solution().divide(dividend, divisor)
    print(f"ER: {result}\nAR: {res}" if res != result else "Passed", "\n")


test(10, 3, 3)
test(7, -3, -2)
test(-2147483648, 1, -2147483648)
test(2147483647, 1, 2147483647)
