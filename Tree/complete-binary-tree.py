from collections import deque

# Definition of a binary tree node
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isCompleteTree(self, root):
        if root is None:
            return True

        nullfound = False
        queue = deque([root])

        while queue:
            t = queue.popleft()

            if t is None:
                nullfound = True
            else:
                if nullfound:
                    return False

                queue.append(t.left)
                queue.append(t.right)

        return True

    def list_to_tree(self, arr):
        if not arr or arr[0] is None:
            return None

        root = TreeNode(arr[0])
        queue = deque([root])
        i = 1

        while queue and i < len(arr):
            node = queue.popleft()

            if i < len(arr):
                if arr[i] is not None:
                    node.left = TreeNode(arr[i])
                    queue.append(node.left)
                i += 1

            if i < len(arr):
                if arr[i] is not None:
                    node.right = TreeNode(arr[i])
                    queue.append(node.right)
                i += 1

        return root


root = [1, 2, 3, 4, 5, 6]

solution = Solution()
root = solution.list_to_tree(root)

print(solution.isCompleteTree(root))