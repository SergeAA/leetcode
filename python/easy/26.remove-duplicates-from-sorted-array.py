from utils import List

# @lc code=start


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not len(nums):
            return 0
        cnt = 1
        for cur in range(1, len(nums)):
            if nums[cur] > nums[cnt - 1]:
                nums[cnt] = nums[cur]
                cnt += 1
        return cnt

    # this is the fastest way to do it
    # def removeDuplicates(self, nums: List[int]) -> int:
    #     nums[:] = sorted(set(nums))
    #     return len(nums)


# @lc code=end

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
expectedNums = [0, 1, 2, 3, 4]

k = Solution().removeDuplicates(nums)

assert k == len(expectedNums)
for i in range(k):
    assert nums[i] == expectedNums[i]
