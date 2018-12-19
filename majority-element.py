#coding=utf-8
"""
给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:

输入: [3,2,3]
输出: 3
示例 2:

输入: [2,2,1,1,1,2,2]
输出: 2


"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dicts={}
        for i in nums:
            if i in num_dicts:
                num_dicts[i]+=1
            else:
                num_dicts[i]=1
        print(num_dicts)

        # 在对字典进行数据操作的时候，默认只会处理key，而不是value
        # 先使用zip把字典的keys和values翻转过来，再用max取出值最大的那组数据
        # max_prices = max(zip(prices.values(), prices.keys()))
        max_num=max(zip(num_dicts.values(),num_dicts.keys()))
        # return max(num_dicts.keys(),key=lambda x:num_dicts.values())
        return max_num[1] #返回的也是一个字典

if __name__ == "__main__":
    print Solution().majorityElement([1, 2, 3, 4, 5, 5, 5, 5, 5, 5, 6])

