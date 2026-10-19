class Solution(object):
    def buildTree(self, preorder, inorder):
        
        f = {}

        for i in range(len(inorder)):
            f[inorder[i]] = i

        idx = [0]

        def fun(low , high):
            if low > high:
                return None
                
            node = TreeNode(preorder[idx[0]])
            idx[0] += 1

            id = f[node.val]

            node.left = fun(low , id - 1)
            node.right= fun(id + 1 , high)

            return node

        return fun(0, len(inorder) - 1)

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
solution = Solution()
root = solution.buildTree(preorder, inorder)