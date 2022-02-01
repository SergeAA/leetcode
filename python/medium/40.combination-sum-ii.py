from typing import List
from utils import testtime

# not mine
# @lc code=start


class Solution:
    # @testtime(10000)
    def combinationSum2(
        self, candidates: List[int], target: int
    ) -> List[List[int]]:
        candidates.sort()
        res = []

        def _recurse(selected, idx, total):
            if total == target:
                res.append([e for e in selected])
            elif total < target:
                for i in range(idx, len(candidates)):
                    if i > idx and candidates[i] == candidates[i - 1]:
                        continue
                    nt = total + candidates[i]
                    if nt > target:
                        break
                    selected.append(candidates[i])
                    _recurse(selected, i + 1, nt)
                    selected.pop()

        _recurse([], 0, 0)
        return res


# @lc code=end


def test(er, *args):
    ar = Solution().combinationSum2(*args)
    print(f"ER: {er}\nAR: {ar}" if ar != er else "Passed", "\n")


test([[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]], [10, 1, 2, 7, 6, 1, 5], 8)
test([[1, 2, 2], [5]], [2, 5, 2, 1, 2], 5)
test([], [2], 1)
test([[1]], [1], 1)

test(
    [
        [6, 6, 7, 8],
        [6, 7, 14],
        [6, 8, 13],
        [6, 9, 12],
        [6, 10, 11],
        [6, 21],
        [7, 8, 12],
        [7, 9, 11],
        [7, 20],
        [8, 8, 11],
        [8, 9, 10],
        [9, 9, 9],
        [9, 18],
        [10, 17],
        [11, 16],
        [13, 14],
        [27],
    ],
    [
        14,
        6,
        25,
        9,
        30,
        20,
        33,
        34,
        28,
        30,
        16,
        12,
        31,
        9,
        9,
        12,
        34,
        16,
        25,
        32,
        8,
        7,
        30,
        12,
        33,
        20,
        21,
        29,
        24,
        17,
        27,
        34,
        11,
        17,
        30,
        6,
        32,
        21,
        27,
        17,
        16,
        8,
        24,
        12,
        12,
        28,
        11,
        33,
        10,
        32,
        22,
        13,
        34,
        18,
        12,
    ],
    27,
)


test(
    [],
    [
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
        1,
    ],
    27,
)
