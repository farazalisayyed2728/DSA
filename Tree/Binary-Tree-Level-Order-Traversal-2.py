from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        res = []
        queue = deque([root]) 

        while queue :
            level = []
            size = len(queue)

            for i in range(size):
                node = queue.popleft()
                
                if node is None :
                    continue

                level.append(node.val)

                if node.left is not None:
                    queue.append(node.left)

                if node.right is not None:
                    queue.append(node.right)

            if level:
                res.append(level)

        return res[::-1]
        