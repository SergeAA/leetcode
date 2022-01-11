from utils import (
    testtime,
    Optional,
    ListNode,
    convert_list_to_listnode,
    convert_listnode_to_list,
)

# @lc code=start


class Solution:
    @testtime(1000)
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv = top = ListNode()
        top.next = head

        while head and head.next:
            prv.next, head.next = head.next, head.next.next
            prv.next.next, prv, head = head, head, head.next

        return top.next


# @lc code=end


def test(input, result):
    head = convert_list_to_listnode(input)
    sol = Solution().swapPairs(head)
    res = convert_listnode_to_list(sol)
    print(f"ER: {result}\nAR: {res}" if res != result else "Passed", "\n")


test([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5])
test([1, 2, 3], [2, 1, 3])
test([1, 2, 3, 4], [2, 1, 4, 3])
test([], [])
test([1], [1])
