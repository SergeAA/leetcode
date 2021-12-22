#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        start = None
        prev = None
        n = 0
        while True:
            val = l1.val + l2.val + n
            if val >= 10:
                n = 1
                val -= 10
            else:
                n = 0

            ln = ListNode(val)
            if not start:
                start = ln
            if prev:
                prev.next = ln

            if (not l1.next) and (not l2.next):
                if n:
                    ln.next = ListNode(n)
                break

            prev = ln
            l1 = l1.next if l1.next else ListNode(0)
            l2 = l2.next if l2.next else ListNode(0)

        return start

# @lc code=end
