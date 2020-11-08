# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""

"""
两个从小到大的数组，找到中位数，要求时间复杂度 O(log(m+n))

nums1 = [2], nums2 = []
return 2.0000
"""

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        nLen = len(nums1) + len(nums2)
        mid = nLen // 2
        newArr = []

        pass