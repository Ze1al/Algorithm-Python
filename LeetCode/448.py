# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
"""

"""
查看数组中那个数字不存在
"""


class Solution:
    def findDisappearedNumbers(self, nums):
        res = []
        for i in range(0, len(nums)):
            index = abs(nums[i])-1
            if nums[index] > 0:
                nums[index] *= -1
        for i in range(0 , len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res



if __name__ == "__main__":
    Solution = Solution()
    print(Solution.findDisappearedNumbers([4,3,2,7,8,2,3,1]))