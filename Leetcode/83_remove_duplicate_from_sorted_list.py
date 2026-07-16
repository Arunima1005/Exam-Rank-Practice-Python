# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lst = []
        node = head
        prev = node
        while node is not None:
            if node.val not in lst:
                lst.append(node.val)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next
        return head
## Can use Set()

### seen = set()
### if node.val not in seen:

##----------------------------------------------
##### Another way -- as sorted list already

# class Solution:
#     def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         current = head

#         while current and current.next:
#             if current.val == current.next.val:
#                 current.next = current.next.next
#             else:
#                 current = current.next

#         return head


s = Solution()
l = ListNode(3, ListNode(8, ListNode(3, (ListNode(9, ListNode(2, ListNode(5, ListNode(3))))))))
result = s.deleteDuplicates(l)
while result is not None:
    print(result.val)
    result = result.next