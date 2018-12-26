#coding=utf-8
"""
给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。

示例 1:

输入: [1,2,3]
输出: 6
示例 2:

输入: [1,2,3,4]
输出: 24
注意:

给定的整型数组长度范围是[3,104]，数组中所有的元素范围是[-1000, 1000]。
输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。

即先将数组排序，我们假设数组够长，那么可能数组最左边三个是绝对值比较大的三个负数，数组最大值肯定要求正数，
那么则有两种可能：取最右边三个或者最左边两个乘最右边一个   ，最后比较这两种情况取最大值即为所要求的值
"""
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #排序，reverse为正,则从大到小排序，若为False，则从小到大排序
        nums.sort(reverse=True)
        #将最大的三个数相乘
        res1=nums[0]*nums[1]*nums[2]
        #最大的数和最小的两个数相乘
        res2=nums[0]*nums[-1]*nums[-2]
        #返回两者中最大的值
        return max(res1,res2)

if __name__ == "__main__":
    print Solution().maximumProduct([1,2,3])
    
