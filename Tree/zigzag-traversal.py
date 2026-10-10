# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """

        if root is None:
            return []

        res = []
        queue = deque([root])
        left_to_right = 1

        while queue :
            size = len(queue)

            level = [None] * size
            first = 0
            last = size - 1

            for i in range(size):
                node = queue.popleft()


                if left_to_right == 1:
                    level[first] = node.val
                    first += 1

                else:
                    level[last] = node.val
                    last -= 1

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            
            res.append(level)

            left_to_right = 1 - left_to_right

        return res