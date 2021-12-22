from utils import List

# @lc code=start


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        cnt = 0
        for cur in range(0, len(nums)):
            if nums[cur] != val:
                nums[cnt] = nums[cur]
                cnt += 1
        return cnt

    # this is the fastest way to do it
    # def removeElement(self, nums: List[int], val: int) -> int:
    #     try:
    #         while nums.index(val):
    #             nums.remove(val)
    #     except Exception:
    #         return len(nums)


# @lc code=end

nums = [0, 1, 2, 2, 3, 0, 4, 2, 2, 2, 2, 2]
val = 2
expectedNums = [0, 0, 1, 3, 4]

k = Solution().removeElement(nums, val)

assert k == len(expectedNums)
nums[:] = sorted(nums[:k])
for i in range(k):
    assert nums[i] == expectedNums[i]
