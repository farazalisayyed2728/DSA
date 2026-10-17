from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def isCompleteTree(self, root):
        if root is None:
            return True

        queue = deque([root])
        gap_found = False

        while queue:
            node = queue.popleft()

            if node is None:
                gap_found = True
            else:
                if gap_found:
                    return False
                queue.append(node.left)
                queue.append(node.right)

        return True


def build_tree(values):
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if node is not None:
            node.left = TreeNode(values[i]) if values[i] is not None else None
            i += 1
            queue.append(node.left)

            if i < len(values):
                node.right = TreeNode(values[i]) if values[i] is not None else None
                i += 1
                queue.append(node.right)

    return root


root = build_tree([1, 2, 3, 4, 5, 6])
print(Solution().isCompleteTree(root))  # True