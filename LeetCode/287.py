# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""

class Solution:
    def findDuplicate(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i])
            if nums[index] > 0:
                nums[index] *= -1
            else:
                return index


if __name__ == "__main__":
    Solution = Solution()
    print(Solution.findDuplicate([1,3,4,2,2]))

