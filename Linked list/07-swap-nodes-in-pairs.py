# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return head

        left = head
        res = None
        preleft = None
        size = 2
        
        right = None

        while True:
            right = left

            for i in range(size-1):
                if right is None:
                    break

                right = right.next

            if right is None:
                if preleft:
                    preleft.next = left
                break

            nextleft = right.next


            right.next = left
            left.next = nextleft

            if res is None:
                res = right

            if preleft:
                preleft.next = right

            
            preleft = left

            left = nextleft

        return res