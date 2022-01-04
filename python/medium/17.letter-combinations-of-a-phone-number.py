from typing import List
from re import sub
from itertools import product
from utils import testtime

CNT = 10000
# @lc code=start


class Solution:
    letters = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

    @testtime(CNT)
    def letterCombinations2(self, digits: str) -> List[str]:
        res, ln = digits, len(digits) - 1
        for i, l in enumerate(digits):
            pat = "(" + r"\S" * i + f")({l})(" + r"\S" * (ln - i) + ")"
            res = " ".join(
                [
                    sub(pat, r"\1" + a + r"\3", res)
                    for a in self.letters[int(l) - 2]
                ]
            )
        return res.split()

    @testtime(CNT)
    def letterCombinations(self, digits: str) -> List[str]:
        d = {
            "2": ("a", "b", "c"),
            "3": ("d", "e", "f"),
            "4": ("g", "h", "i"),
            "5": ("j", "k", "l"),
            "6": ("m", "n", "o"),
            "7": ("p", "q", "r", "s"),
            "8": ("t", "u", "v"),
            "9": ("w", "x", "y", "z"),
        }

        return ["".join(t) for t in product(*map(d.get, digits)) if t]


# @lc code=end

assert sorted(Solution().letterCombinations("23")) == [
    "ad",
    "ae",
    "af",
    "bd",
    "be",
    "bf",
    "cd",
    "ce",
    "cf",
]

print(Solution().letterCombinations(""))
print(Solution().letterCombinations("2"), ["a", "b", "c"])
