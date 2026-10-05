# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # ans = set()
        # dummy = head
        # while dummy:
        #     ans.add(dummy)
        #     nextval = dummy.next
        #     if nextval == None:
        #         return False
        #     if nextval in ans:
        #         return True
        #     dummy = dummy.next
        # return False

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False