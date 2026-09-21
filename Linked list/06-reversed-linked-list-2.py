# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        
        if head is None :
            return None

        if left == right:
            return head

        before = None
        t = head
        pos = 1

        while t is not None:
            if pos < left:
                before = t
                t = t.next
                pos += 1
                continue

            cur = t
            pre = None
            times = right - left + 1

            while times > 0:
                next_node = cur.next
                cur.next = pre
                pre = cur
                cur = next_node
                times -= 1

            t.next = cur


            if before is not None :
                before.next = pre

            else:
                head = pre

            break

        return head

head = [1,2,3,4,5]
left = 2
right = 4
solution = Solution()
result = solution.reverseBetween(head, left, right)