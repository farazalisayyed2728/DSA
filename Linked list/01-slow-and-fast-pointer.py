# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        slow = head
        fast = head
        
        
        while fast != None and fast.next is not None:
            slow = slow.next

            fast = (fast.next.next)
            if slow == fast:
                return True

            elif fast == None:
                return False
head = [3,2,0,-4]
solution = Solution()
result = solution.hasCycle(head)
print(result)
