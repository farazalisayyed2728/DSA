class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = [0]
        def height(node):
            if node is None :
                return 0

            left = height(node.left)
            right = height(node.right)
            
            res[0] = max(res[0], left + right)

            return 1 + max(left , right)
        height(root)
        return res[0]
    
        
        