# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""

"""
两个从小到大的数组，找到中位数，要求时间复杂度 O(log(m+n))

nums1 = [2], nums2 = []
return 2.0000

取中位数字，k/2-1的值
"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        def getKthelement(k):
            # index point
            index_1, index_2 = 0, 0
            while True:
                # special condition
                if m == index_1:
                    return nums2[index_2 + k - 1]
                if n == index_2:
                    return nums1[index_1 + k - 1]
                # exit
                if k == 1:
                    return min(nums1[int(index_1)], nums2[int(index_2)])

                # normal
                temp_index_1 = min(index_1 + k // 2 - 1, m - 1)
                temp_index_2 = min(index_2 + k // 2 - 1, n - 1)
                # nums1 < nums2
                if nums1[int(temp_index_1)] <= nums2[int(temp_index_2)]:
                    k -= temp_index_1 - index_1 + 1
                    index_1 = temp_index_1 + 1
                else:
                    k -= temp_index_2 - index_2 + 1
                    index_1 = temp_index_2 + 1

        m, n = len(nums1), len(nums2)
        if (m + n) % 2 == 1:
            return getKthelement((m + n + 1) // 2)
        else:
            return (getKthelement((m + n) // 2) + getKthelement((m + n) // 2 + 1)) / 2


if __name__ == "__main__":
    Solution = Solution()
    nums1 = [1, 3, 4, 9]
    nums2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(Solution.findMedianSortedArrays(nums1, nums2))
