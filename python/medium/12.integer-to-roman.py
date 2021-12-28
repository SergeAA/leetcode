from time import time

# @lc code=start


class Solution:
    roman = {
        1000: "M",
        900: "CM",
        500: "D",
        400: "CD",
        100: "C",
        90: "XC",
        50: "L",
        40: "XL",
        10: "X",
        9: "IX",
        5: "V",
        4: "IV",
        1: "I",
    }

    def intToRoman(self, num: int) -> str:
        res = ""
        for k, v in self.roman.items():
            if num // k:
                return res + v * (num // k) + self.intToRoman(num % k)
        return res


# @lc code=end

t = [3, 4, 9, 42, 30, 401, 945, 1994, 3999]
r = ["III", "IV", "IX", "XLII", "XXX", "CDI", "CMXLV", "MCMXCIV", "MMMCMXCIX"]

z = time()
for i in range(len(t)):
    s = Solution().intToRoman(t[i])
    print(t[i], s)
    assert s == r[i]
print(f"Time: {time()-z:0.2f}")
