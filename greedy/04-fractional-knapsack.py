class Solution:
    def fractionalKnapsack(self, val, wt, capacity):

        n = len(val)

        arr = []

        for i in range(n):
            ratio = val[i] / wt[i]
            arr.append((ratio, val[i], wt[i]))

        # Sort by value/weight ratio in descending order
        arr.sort(reverse=True)

        res = 0

        for ratio, value, weight in arr:

            if capacity >= weight:
                res += value
                capacity -= weight

            else:
                res += ratio * capacity
                break

        return res

val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50
solution = Solution()
print(solution.fractionalKnapsack(val, wt, capacity))