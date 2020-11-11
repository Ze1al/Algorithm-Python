# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""

"""
最长回文子串
"""
class Solution:
    def longestPalindrome(self, s):
        n = len(s)
        dp = [[False]*n for i in range(n)]
        res = ""
        for i in range(n):
            for j in range(n):
                # i > j
                if i < j:
                    break
                # len =1
                if i == j:
                    dp[i][j] = True
                # len = 2
                if i - j == 1 and s[i]==s[j] :
                    dp[i][j] = True
                # len > 2
                if i - j >= 2:
                    if s[i]==s[j] and dp[i-1][j+1] == True:
                        dp[i][j] = True
                if dp[i][j] == True and i-j+1>len(res):
                    res = s[j:i+1]
        return res



if __name__ == '__main__':
    Solution = Solution()
    s = "ddcdcd"
    print(Solution.longestPalindrome(s))

