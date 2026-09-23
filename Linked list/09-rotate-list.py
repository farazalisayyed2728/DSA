# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """

        if head is None or head.next is None :
            return head

        last = head
        n = 1


        while last.next is not None :
            n += 1
            last = last.next

        k = k % n
        if k == 0:
            return head

        
        t = head

        for i in range(n - k - 1):
            t = t.next

        res = t.next

        t.next = None 

        last.next = head

        return res

        

head = [1,2,3,4,5]
k = 2   
solution = Solution()
result = solution.rotateRight(head, k)