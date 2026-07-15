# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        final = []
        # final2 =[]
        while list1 is not None:
            final.append(list1.val)
            list1 = list1.next
        while list2 is not None:
            final.append(list2.val)
            list2 = list2.next
        # print(final.sort())
        # print(final)
        final.sort()
        dummy = ListNode(-1)
        node = dummy
        for value in final:
            node.next = ListNode(value)
            node = node.next
        return dummy.next


# #### Another way -- my verison
# class Solution:
#     def mergeTwoLists(
#         self,
#         list1: Optional[ListNode],
#         list2: Optional[ListNode],
#     ) -> Optional[ListNode]:

#         values = []

#         for head in (list1, list2):
#             while head:
#                 values.append(head.val)
#                 head = head.next

#         values.sort()

#         dummy = ListNode(-1)
#         current = dummy

#         for value in values:
#             current.next = ListNode(value)
#             current = current.next

#         return dummy.next




s = Solution()
l1 = ListNode(1, (ListNode(2, (ListNode(9)))))
l2 = ListNode(1, (ListNode(6, (ListNode(8)))))
merge_list = s.mergeTwoLists(l1,l2)
l = []
while merge_list is not None:
    l.append(merge_list.val)
    merge_list = merge_list.next
print(l)