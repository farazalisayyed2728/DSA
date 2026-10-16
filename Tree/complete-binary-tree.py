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

    
root = [1,2,3,4,5,6]
solution = Solution()
# Assuming you have a function to convert the list representation of the tree into a TreeNode structure
root = solution.list_to_tree(root)
print(solution.isCompleteTree(root))