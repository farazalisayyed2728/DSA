class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.res = None

        def dfs(node):

            if node is None:
                return False

            left = dfs(node.left)
            right = dfs(node.right)
            mid = node in [p,q]
            
            if left+right+mid > 1:
                self.res = node
            
            return left or right or mid
        
        dfs(root)
        return self.res