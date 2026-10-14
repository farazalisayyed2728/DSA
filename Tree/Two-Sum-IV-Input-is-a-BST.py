class Solution(object):

    def getsmall(self, asc):
        if not asc:
            return None

        small = asc.pop()
        rightchild = small.right

        while rightchild:
            asc.append(rightchild)
            rightchild = rightchild.left

        return small

    def getbig(self, dsc):
        if not dsc:
            return None

        big = dsc.pop()
        leftchild = big.left

        while leftchild:
            dsc.append(leftchild)
            leftchild = leftchild.right

        return big

    def findTarget(self, root, k):
        if root is None:
            return False

        asc = []
        dsc = []

        t = root
        while t:
            asc.append(t)
            t = t.left

        t = root
        while t:
            dsc.append(t)
            t = t.right

        small = self.getsmall(asc)
        big = self.getbig(dsc)

        while small and big and small != big:
            total = small.val + big.val

            if total == k:
                return True
            elif total < k:
                small = self.getsmall(asc)
            else:
                big = self.getbig(dsc)

        return False