class Solution(object):
    def hasPathSum(self, root, targetSum):
        def fun(root , currentSum):

            if root is None:
                return False
            
            currentSum += root.val

            if root.left is None and root.right is None :
                return currentSum == targetSum

            return fun(root.left , currentSum) or fun(root.right,  currentSum)


        return fun(root , 0)
        

        