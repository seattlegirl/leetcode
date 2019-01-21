#coding=utf-8
"""
和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。

现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。

示例 1:

输入: [1,3,2,2,5,2,3,7]
输出: 5
原因: 最长的和谐数组是：[3,2,2,2,3].
说明: 输入的数组长度最大不超过20,000.

对数组中每个元素计数，统计相邻大小元素的个数之和，返回最大的值。
        
Counter类的目的是用来跟踪值出现的次数。它是一个无序的容器类型，以字典的键值对形式存储，
其中元素作为key，其计数作为value。计数值可以是任意的Interger（包括0和负数）。
Counter类和其他语言的bags或multisets很相似。
"""
import collections
class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans=0
        counts=collections.Counter(nums)
        for i in counts:
            if i+1 in counts:
                ans= max(ans,counts[i]+counts[i+1])
        return ans

if __name__ == "__main__":
    print Solution().findLHS([1,3,2,2,5,2,3,7])
    
