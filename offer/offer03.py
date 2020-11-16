# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
    给定一个数组，将其中的一个子数组排序，排序后整个数组是有序的
    比较排序排好的数组
"""


class Solution:
    def findUnsortedSubarray(self, nums):
        sortNum = sorted(nums)
        if sortNum == nums:
            return 0
        pre = 0
        last = len(nums) - 1
        while pre < last and nums[pre] == sortNum[pre]:
            pre += 1
        while pre < last and nums[last] == sortNum[last]:
            last -= 1
        return last - pre + 1
