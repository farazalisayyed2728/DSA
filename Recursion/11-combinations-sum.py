class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def fun(idx , diary, total):
            if total == target:
                res.append(diary[:])
                return

            if idx == len(candidates) :
                    return


            fun(idx + 1 , diary , total)

            if total + candidates[idx] <= target :
                diary.append(candidates[idx])

                fun(idx , diary , total + candidates[idx])
                diary.pop()


        fun(0 , [] , 0)

        return res
            
candidates = [2,3,6,7]
target = 7
solution = Solution()
print(solution.combinationSum(candidates, target))