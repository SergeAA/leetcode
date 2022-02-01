from typing import List
from utils import testtime

# @lc code=start


class Solution:
    # @testtime(10000)
    def combinationSum(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        res, ln = [], len(candidates) - 1
        for i, it in enumerate(candidates):
            if it > target:
                continue
            cnt = target // it
            while cnt > 0:
                tmp = [it] * cnt
                nt = target - it * cnt
                if nt == 0:
                    res.append(tmp)
                elif i < ln:
                    rec = self.combinationSum(candidates[i + 1 :], nt)
                    for k in rec:
                        res.append(tmp + k)
                cnt -= 1
        return res


# @lc code=end


def test(er, *args):
    ar = Solution().combinationSum(*args)
    print(f"ER: {er}\nAR: {ar}" if ar != er else "Passed", "\n")


test([[2, 2, 3], [7]], [2, 3, 6, 7], 7)
test([[2, 2, 2, 2], [2, 3, 3], [3, 5]], [2, 3, 5], 8)
test([], [2], 1)


test(
    [
        [1, 1, 1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1, 2],
        [1, 1, 1, 1, 3],
        [1, 1, 1, 2, 2],
        [1, 1, 2, 3],
        [1, 2, 2, 2],
        [1, 3, 3],
        [2, 2, 3],
    ],
    [1, 2, 3],
    7,
)
