from collections import deque
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: Optional[TreeNode]
        """
        if root is None:
            return True
        nullfound = False

        queue = deque([root])

        while queue:
            t = queue.popleft()
            
            if t is None:
                nullfound = True

            else:
                if nullfound :
                    return False

                queue.append(t.left)
                queue.append(t.right)

        return True
        