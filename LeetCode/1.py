# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""

"""
两数之和
"""


class Solution:
    def twoSum(self, nums, target):
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []