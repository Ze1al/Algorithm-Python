# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""


# 求连续数组的最大子序和


class Solution:
    def maxSubArray(self, nums):
        for i in range(1,len(nums)):
            nums[i] = max(nums[i-1]+nums[i],nums[i])
        return max(nums)

