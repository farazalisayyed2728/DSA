class Solution(object):
    def isValidBST(self, root):
        prev = [None]

        def ino(node):

            if node is None:
                return True

            if not ino(node.left):
                return False

            
            if prev[0] is not None and node.val <= prev[0]:
                return False
            
            prev[0] = node.val

            return ino(node.right)

        return ino(root)


root = [2, 1, 3]
s = Solution()
print(s.isValidBST(root))
