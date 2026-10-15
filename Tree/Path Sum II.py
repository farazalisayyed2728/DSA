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

root = [5,4,8,11,None,13,4,7,2,None,None,5,1]
targetSum = 22
solution = Solution()
print(solution.pathSum(root, targetSum))