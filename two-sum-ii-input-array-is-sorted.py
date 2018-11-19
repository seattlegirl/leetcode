"""
给定一个已按照升序排列 的有序数组，找到两个数使得它们相加之和等于目标数。

函数应该返回这两个下标值 index1 和 index2，其中 index1 必须小于 index2。

说明:

返回的下标值（index1 和 index2）不是从零开始的。
你可以假设每个输入只对应唯一的答案，而且你不可以重复使用相同的元素。
示例:

输入: numbers = [2, 7, 11, 15], target = 9
输出: [1,2]
解释: 2 与 7 之和等于目标数 9 。因此 index1 = 1, index2 = 2 。

"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic={}
        for i,number in enumerate(numbers):
            if((target-number) in dic): #字典中的访问是用key键值。这里的(target-number)是dic的键值
                return [dic[target-number]+1,i+1]    
            dic[number]=i

"""
需要注意的是将列表中的元素放入字典时，是将值作为下标，将下标作为值，这样做时有一定意义的。
如果反向了，即使你得到了相对应的值，你也无法知道它的下标是多少，所以这里一定要注意。
"""