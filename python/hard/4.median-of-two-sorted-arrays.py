from utils import List

# @lc code=start


class Solution:
    def findMedianSortedArrays(
        self, nums1: List[int], nums2: List[int]
    ) -> float:
        arr = sorted(nums1 + nums2)
        ln = len(arr)
        if not ln:
            return 0
        cen = ln // 2
        return arr[cen] if ln % 2 else (arr[cen - 1] + arr[cen]) / 2


# @lc code=end

assert Solution().findMedianSortedArrays([], []) == 0
assert Solution().findMedianSortedArrays([1, 3], [2]) == 2
assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
