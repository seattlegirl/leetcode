#coding=utf-8
"""
485. 最大连续1的个数
给定一个二进制数组， 计算其中最大连续1的个数。

示例 1:

输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
注意：

输入的数组只包含 0 和1。
输入数组的长度是正整数，且不超过 10,000。

思路：在一个列表循环中，将连续1个数存取，并每次取最大值
"""
class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a=0
        b=0
        for n in nums:
            if n==1:
                a+=1
            else:
                a=0
            b=max(a,b)
        return b
        
if __name__ == "__main__":
    print Solution().findMaxConsecutiveOnes([1,1,0,0,0,1,1,1,1,0,0])