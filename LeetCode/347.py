# -*- coding:utf-8 -*-

"""
    author   = zengjinlin
    返回前K个高频元素
"""

class Solution:
    def topKFrequent(self, nums, k):
        dict = {}
        for i in nums:
            if i not in dict:
                dict[i] = 1
            else:
                dict[i] += 1
        resList = sorted(dict.items(), key=lambda x: x[1], reverse=True)
        print(resList)
        return [resList[i][0] for i in range(k)]

if __name__ == "__main__":
    Solution = Solution()
    print(Solution.topKFrequent([3,0,1,0], 1))
