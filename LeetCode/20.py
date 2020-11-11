# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""

"""
有效括号

输入: "()[]{}"
输出: true
"""


class Solution:
    def isValid(self, s: str):
        if len(s) % 2 == 1:
            return False
        # 维护一个栈
        stack = []

        pair = {
            "]": "[",
            "}": "{",
            ")": "("
        }

        for i in s:
            if i in pair:
                if not stack or stack[-1] == pair[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)

        if stack:
            return False
        return True