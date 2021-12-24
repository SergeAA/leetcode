from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def convert_list_to_listnode(lst: List) -> Optional[ListNode]:
    if not lst:
        return None
    current = ListNode(lst[0])
    root = current
    for i in lst[1:]:
        current.next = ListNode(i)
        current = current.next
    return root


def convert_listnode_to_list(node: Optional[ListNode]):
    if node is None:
        return []
    res = [node.val]
    while node.next is not None:
        node = node.next
        res.append(node.val)
    return res
