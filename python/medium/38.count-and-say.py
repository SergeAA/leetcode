from utils import testtime

# @lc code=start


class Solution:
    # @testtime(10000)
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        s = self.countAndSay(n - 1)
        l, c, r = s[0], 1, ""
        for i in s[1:]:
            if i != l:
                r += f"{c}{l}"
                c, l = 1, i
            else:
                c += 1
        r += f"{c}{l}"
        return r


# @lc code=end


def test(er, *args):
    ar = Solution().countAndSay(*args)
    print(f"ER: {er}\nAR: {ar}" if ar != er else "Passed", "\n")


test("1", 1)
test("1211", 4)
test("111221", 5)
