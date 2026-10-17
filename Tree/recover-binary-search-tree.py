class Solution(object):
    def recoverTree(self, root):
        prev = [None]
        first = [None]
        second = [None]

        def fun(node):
            if node is None:
                return

            # 1. Traverse left
            fun(node.left)

            # 2. Detect misplaced nodes
            if prev[0] is not None and node.val < prev[0].val:
                if first[0] is None:
                    first[0] = prev[0]

                second[0] = node

            # Update previous node
            prev[0] = node

            # 3. Traverse right
            fun(node.right)

        fun(root)

        # Swap the two misplaced values
        first[0].val, second[0].val = (
            second[0].val, first[0].val
        )