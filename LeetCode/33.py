# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""

class Solution:
    def search(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            return -1