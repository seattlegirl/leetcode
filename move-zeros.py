#coding=utf-8
"""
283. 移动零

给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

示例:

输入: [0,1,0,3,12]
输出: [1,3,12,0,0]
说明:

必须在原数组上操作，不能拷贝额外的数组。
尽量减少操作次数。
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n=nums.count(0) #统计字符串里字符0出现的次数
        for i in range(n):
            nums.remove(0) #移除列表中0的第一个匹配项
        nums.extend([0]*n) #函数用于在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）。
        return nums

if __name__ == "__main__":
    print Solution().moveZeroes([0,1,0,3,12])
    
