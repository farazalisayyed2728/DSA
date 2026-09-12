class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        slow = head
        fast = head

        # Step 1: Detect cycle
        while fast is not None and (fast.next) is not None:

            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break
        else:
            return None

        # Step 2: Find cycle starting point
        slow = head

        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow

head = [3,2,0,-4]
solution = Solution()
result = solution.detectCycle(head)
print(result)