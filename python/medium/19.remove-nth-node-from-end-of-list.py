from utils import (
    testtime,
    Optional,
    ListNode,
    convert_list_to_listnode,
    convert_listnode_to_list,
)

# @lc code=start


class Solution:
    def removeNthFromEnd(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        # set fast and slow pointers
        fast = head
        slow = head

        # fast moves n + 1 steps
        while n > 0:
            fast = fast.next
            n -= 1

        # if after moving forward n + 1 steps, fast reaches the None
        # then the nth node is just the first node of head
        if fast == None:
            return head.next

        # move slow and fast pointer at the same time until fast reaches the end
        # then the node after the slow pointer is the one to be removed
        while fast.next != None:
            fast = fast.next
            slow = slow.next

        # connect the slow pointer and the node after the next node
        nxt = slow.next
        slow.next = nxt.next

        return head

    def removeNthFromEnd2(
        self, head: Optional[ListNode], n: int
    ) -> Optional[ListNode]:
        if not head:
            return None

        node, cnt = head, 0
        while node:
            cnt += 1
            node = node.next

        if cnt - n == 0:
            return head.next

        node = prev = head
        for _ in range(cnt - n):
            prev, node = node, node.next

        prev.next = node.next
        return head


# @lc code=end


def test(input, n, result):
    head = convert_list_to_listnode(input)
    sol = Solution().removeNthFromEnd(head, n)
    res = convert_listnode_to_list(sol)
    print(f"ER: {result}\nAR: {res}" if res != result else "Passed", "\n")


test([1], 1, [])
test([1, 2], 2, [2])
test([1, 2], 1, [1])
test([1, 2, 3, 4, 5], 2, [1, 2, 3, 5])
