class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sumNumbers(self, root):
        def fun(root, currentSum):
            if root is None:
                return 0

            currentSum = currentSum * 10 + root.val

            if root.left is None and root.right is None:
                return currentSum

            return fun(root.left, currentSum) + fun(root.right, currentSum)

        return fun(root, 0)


# Create Tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

# Create Solution object
s = Solution()

# Call function
print(s.sumNumbers(root))