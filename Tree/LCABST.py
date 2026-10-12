# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        if root is None:
            return None

        if root == p or root == q:
            return root

        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)


        elif  root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left , p,q)

        else:
            return root
        
root = [6,2,8,0,4,7,9,None,None,3,5]
p = 2
q = 8
solution = Solution()
result = solution.lowestCommonAncestor(root, p, q)