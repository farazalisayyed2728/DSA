class Solution(object):
    def maximumSum(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        nodel = arr[0]
        onedel = float('-inf')
        res = arr[0]

        for i in range(1, len(arr)):
            previous_nodel = nodel
            previous_onedel = onedel

            if previous_onedel == float('-inf'):
                v2 = arr[i]

            else:
                v2 = previous_onedel + arr[i]

            nodel = max(nodel + arr[i] , arr[i])
            onedel = max(v2 , previous_nodel)

            res = max(res, nodel)
            res = max(res, onedel)

        return res