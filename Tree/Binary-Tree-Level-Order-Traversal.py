# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None :
            return []

        res = []
        queue = deque([root])

        while queue :
            level = []
            size = len(queue)

            for i in range(size):
                node = queue.popleft()

                if node is None:
                    continue

                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            if level:
                res.append(level)

        return res


        
        