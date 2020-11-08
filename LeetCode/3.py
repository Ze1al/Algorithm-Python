# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""

"""
无重复字符的最长子串
贪心算法的典型代表
维护一个移动窗口，保持窗口中的值不重复
"abcabcbb"
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0 or len(s) == 1:
            return len(s)
        maxLen = 0
        for i in range(0, len(s)):
            window = [s[i]]
            for j in range(i+1, len(s)):
                if s[j] not in window:
                    window.append(s[j])
                else:
                    break
            if len(window) > maxLen:
                maxLen = len(window)
        return maxLen

if __name__ == '__main__':
    Solution = Solution()
    s = "au"
    print(Solution.lengthOfLongestSubstring(s))



