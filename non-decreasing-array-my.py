"""
给定一个长度为 n 的整数数组，你的任务是判断在最多改变 1 个元素的情况下，该数组能否变成一个非递减数列。

我们是这样定义一个非递减数列的： 对于数组中所有的 i (1 <= i < n)，满足 array[i] <= array[i + 1]。

示例 1:

输入: [4,2,3]
输出: True
解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。
示例 2:

输入: [4,2,1]
输出: False
解释: 你不能在只改变一个元素的情况下将其变为非递减数列。
说明:  n 的范围为 [1, 10,000]。
"""
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        首先题目比较明确，但是却容易出错。找到array[i] > array[i+1]的情况时，需要对二者进行修改，要么修改array[i]，要么修改array[i+1]，如：[3,5,2,4]，         如不修改，则判断为真，实则为假；
        具体是对array[i]做修改还是对array[i+1]做修改，需要判断array[i-1]和array[i+1]两者的大小，具体分两种情况
        情况一：[2,5,3,4]，当i=1时，array[i]=5，此时array[i-1]=2 < array[i+1]=3，则需修改“5”为“3”，即令array[i]=array[i+1]，则保证数组返回真；
        情况二：[4,5,3,7]，当i=1时，array[i]=5，此时array[i-1]=4 > array[i+1]=3，则需修改“3”为“5”，即令array[i+1]=array[i]，则保证数组返回真；
        加入count<=1的判断条件在遍历循环中，只要数组中出现两次修改，则退出，避免后面不必要的计算。

        """
        count=0
        for i in range(0,len(nums)-1):
            
            if(nums[i]>nums[i+1] and count<=1):
                count+=1
                if(i-1<0):
                    nums[i]=nums[i+1]
                if(nums[i-1]<nums[i+1]):
                    nums[i]=nums[i+1]
                if(nums[i-1]>nums[i+1]):
                    nums[i+1]=nums[i]
                    
        return count<=1

