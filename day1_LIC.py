# def longestCommonSubsequence(text1: str, text2: str) -> int:   
    
    
#     for j in range(len(text1)):
#         for i in range(len(text2)):
#             if text1[j] == text2[i]:
#                 lcs += 1
#                 if len(text2) == 1:
#                     print(lcs)
#                     return lcs
#                 return longestCommonSubsequence(text1[j:], text2[i:])
#     print( lcs)

class Solution:
    def longestCommonSubsequence(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)
        if m < n:
            return self.longestCommonSubsequence(s2, s1)
        memo = [[0 for _ in range(n + 1)] for _ in range(2)]

        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    memo[1 - i % 2][j + 1] = 1 + memo[i % 2][j]
                else:
                    memo[1 - i % 2][j + 1] = max(memo[1 - i % 2][j], memo[i % 2][j + 1])

        return memo[m % 2][n]


test = Solution()
a = test.longestCommonSubsequence("ezupkr", "ubmrapg")
