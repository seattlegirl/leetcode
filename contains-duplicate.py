#coding=utf-8
"""
217. 存在重复元素

给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。

示例 1:

输入: [1,2,3,1]
输出: true
示例 2:

输入: [1,2,3,4]
输出: false
示例 3:

输入: [1,1,1,3,3,4,3,2,4,2]
输出: true

"""
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        #方法一：集合（set）是一个无序的不重复元素序列。
        # return len(nums)!=len(set(nums))
        
        #方法二：
        if len(nums)==0 or len(nums)==1:
            return False
        d={}
        for i in nums:
            if i in d:#判断的是键值
                return True
            d[i]=0
        return False

if __name__ == "__main__":
    print Solution().containsDuplicate([1,2,5,9,1])
        