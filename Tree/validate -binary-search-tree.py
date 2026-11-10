class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        prev = [None]

        def ino(node):

            if node is None:
                return True

            if not ino(node.left):
                return False

            if prev[0] is not None and node.val <= prev[0]:
                return False

            prev[0] = node.val

            return ino(node.right)

        return ino(root)


# Construct Binary Tree
root = TreeNode(2)
root.left = TreeNode(1)
root.right = TreeNode(3)

s = Solution()
print(s.isValidBST(root))