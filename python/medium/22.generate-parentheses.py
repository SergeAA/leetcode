from utils import testtime, List


# @lc code=start

# def generateParenthesis(self, n: int) -> List[str]:
#     def gen(string = "", opens = 0, closes = 0):
#         if closes > opens or opens > n:
#             return []
#         if len(string) == (2 * n):
#             return [string]
#         return gen(string + "(", opens + 1, closes) + gen(string + ")", opens, closes + 1)

#     return gen()
class Solution:
    @testtime(10)
    def generateParenthesis(self, n: int) -> List[str]:
        def kret(n):
            if not n:
                return set()
            if n == 1:
                return {"()"}
            if n == 2:
                return {"(())", "()()"}

            res = set()
            for i in range(1, n):
                for t in kret(n - i):
                    res.update({"()" * i + f"({t})", f"({t})" + "()" * i})
            for t in kret(n - 1):
                res.update({f"({t})"})
            return res

        return kret(n)


# @lc code=end


def test(n, result):
    res = Solution().generateParenthesis(n)
    res = sorted(res)
    result = sorted(result)
    print(f"ER: {result}\nAR: {res}" if res != result else "Passed", "\n")


# test(2, ["(())", "()()"])

# test(3, ["((()))", "(()())", "(())()", "()(())", "()()()"])
test(
    4,
    [
        "(((())))",
        "((()()))",
        "((())())",
        "((()))()",
        "(()(()))",
        "(()()())",
        "(()())()",
        "(())(())",
        "(())()()",
        "()((()))",
        "()(()())",
        "()(())()",
        "()()(())",
        "()()()()",
    ],
)
# test(1, ["()"])
