# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""

class Solution:
    def climbStairs(self, n):
        pre = 0
        mid = 0
        last = 1
        for i in range(n):
            pre = mid
            mid = last
            last = pre + mid
        return last
