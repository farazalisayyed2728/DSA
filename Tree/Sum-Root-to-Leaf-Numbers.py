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