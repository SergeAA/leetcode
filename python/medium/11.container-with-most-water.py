from typing import List
from time import time
from utils import bigintarray, task11

# @lc code=start


class Solution:
    def maxArea(self, height: List[int]) -> int:
        mx, l, r = 0, 0, len(height) - 1
        while l < r:
            if min(height[l], height[r]) * (r - l) > mx:
                mx = min(height[l], height[r]) * (r - l)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return mx

    # def maxArea(self, height: List[int]) -> int:
    #     mx = 0
    #     for i in range(len(height) - 1):
    #         for j in range(i + 1, len(height)):
    #             if mx < min(height[i], height[j]) * (j - i):
    #                 mx = min(height[i], height[j]) * (j - i)
    #     return mx


# @lc code=end

print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
z = time()
for i in range(1):
    s = Solution().maxArea(bigintarray)
    if s != task11:
        print("error", s)
        break
print(f"Time: {time()-z}")
