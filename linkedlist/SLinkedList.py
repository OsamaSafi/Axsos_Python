# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(0)
        current = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return dummy.next
    
    def print_list(node):
        values = []
        while node:
            values.append(str(node.val))
            node = node.next
        print(" -> ".join(values))


l1 = ListNode(1, ListNode(2, ListNode(3)))
l2 = ListNode(1, ListNode(2, ListNode(4)))

sol = Solution()
merged_head = sol.mergeTwoLists(l1, l2)
sol = Solution()