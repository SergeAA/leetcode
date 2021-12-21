#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

from utils import (
    Optional,
    ListNode,
    convert_list_to_listnode,
    convert_listnode_to_list,
)

# @lc code=start


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        root = cur = ListNode(0, None)

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                cur.next = ListNode(list1.val, None)
                list1 = list1.next
            else:
                cur.next = ListNode(list2.val, None)
                list2 = list2.next
            cur = cur.next

        cur.next = list1 if list1 is not None else list2

        return root.next


# @lc code=end

list1 = convert_list_to_listnode([-5, 1, 2, 4])
list2 = convert_list_to_listnode([-100, -2, 1, 1, 2, 3, 3, 3, 5])

a = Solution()

res = convert_listnode_to_list(a.mergeTwoLists(list1, list2))
print(res)
