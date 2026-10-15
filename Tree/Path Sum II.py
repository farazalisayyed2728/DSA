# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        result = []

        def dfs(node ,path, currsum):
            if not node:
                return

            path.append(node.val)
            currsum += node.val

            if node.left is None and node.right is None:
                if currsum == targetSum:
                    result.append(path[:])

            else:
                dfs(node.left, path, currsum)
                dfs(node.right, path, currsum)

            path.pop()


        dfs(root, [] , 0)
        return result
