from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def zigzagLevelOrder(self, root):

        if root is None:
            return []

        res = []
        queue = deque([root])
        left_to_right = 1

        while queue:
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


# Construct Binary Tree
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

solution = Solution()
print(solution.zigzagLevelOrder(root))