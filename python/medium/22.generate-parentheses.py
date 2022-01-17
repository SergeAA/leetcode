from utils import testtime, List

# // it is NOT MY solution //

# @lc code=start


class Solution:
    @testtime(10000)
    def generateParenthesis(self, n: int) -> List[str]:
        ht = {}
        ht[1] = set()
        ht[1].add("()")

        for i in range(2, n + 1):
            ht[i] = set()

            for n_minus_1_result in ht[i - 1]:
                ht[i].add("(" + n_minus_1_result + ")")

            for x_idx in range(1, i):
                for x in ht[x_idx]:
                    for y in ht[i - x_idx]:
                        ht[i].add(x + y)
                        ht[i].add(y + x)

        return ht[n]


# @lc code=end


def test(n, result):
    res = Solution().generateParenthesis(n)
    res = sorted(res)
    result = sorted(result)
    print(f"ER: {result}\nAR: {res}" if res != result else "Passed", "\n")


test(2, ["(())", "()()"])

test(3, ["((()))", "(()())", "(())()", "()(())", "()()()"])
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
test(1, ["()"])
