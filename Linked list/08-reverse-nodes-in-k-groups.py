# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if head is None or head.next is None:
            return head

        left = head
        res = None
        preleft = None
        size = k

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
            
            prev = nextleft
            curr = left

            while curr != nextleft:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp


            if res is None:
                res = right


            if preleft:
                preleft.next = right

            
            preleft = left

            left = nextleft

        return res


head = [1,2,3,4,5]
k = 2
solution = Solution()
result = solution.reverseKGroup(head, k)