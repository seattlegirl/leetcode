#coding=utf-8
"""
给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

示例：

给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
说明:

你可以假设数组不可变。
会多次调用 sumRange 方法。
"""

# 超时！！！！！！！！！！！！！！！！！
# class NumArray:

#     def __init__(self, nums):
#         """
#         :type nums: List[int]
#         """
#         self.num=[0]*len(nums)
#         for w in range(len(nums)):
#             self.num[w]=nums[w]
        
        

#     def sumRange(self, i, j):
#         """
#         :type i: int
#         :type j: int
#         :rtype: int
#         """
#         sum=0
#         for k in range(i,j+1):
#             sum+=self.num[k]
#         return sum

#先求出0~j 的和保存起来，然后 (i~j) = (0~j) - (0~i)，这个方式，在多次调用时，效率比较高。
class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        for i in range(1,len(nums)):
            nums[i]+=nums[i-1]
        self.nums=nums
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i==0:
            return self.nums[j]
        return self.nums[j]-self.nums[i-1]


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
numArray = NumArray(nums)
print(numArray.sumRange(0, 1))
print(numArray.sumRange(1, 2))