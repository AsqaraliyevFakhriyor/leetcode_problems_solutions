list_lis = [5, 2, 8, 6, 3, 6, 9, 5]
"""
lis => a1 < a2 < a3 < a5 < ... < an =>
"""

class Solution:
    def __init__(self, list_lis) -> None:
        self.list = list_lis

    def lis(self):
        L =[1] * len(self.list)
        print(L, "\n")
        # print(L)

        for i in range(1, len(L)):
            subproblems = [L[k] for k in range(i) if self.list[k] < self.list[i]]
            print("subproblems: ", subproblems)
            L[i] = 1 + max(subproblems, default=0)
            print(f"L[{i}]: ",L[i])
            print("L => ",L, "\n")
        print(max(L, default=0))
        return max(L, default=0)

solution = Solution(list_lis)

solution.lis()

    