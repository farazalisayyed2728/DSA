# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """

        def fun(root1 , root2):

            if root1 is None and root2 is None:
                return True

            if root1 is None or root2 is None:
                return False

            if root1.val != root2.val :
                return False

            r1 = fun(root1.left, root2.right)        
            r2 = fun(root1.right, root2.left)

            return r1 and r2     


        return fun(root.left , root.right)   