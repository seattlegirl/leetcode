"""
假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
示例 2:

输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
注意:

数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        判断连续0的个数嘛，再根据连续0的个数，判断这个区域能种多少花

        如果0的连续个数n>2,那么这个地方就能种（n-1）/2朵花

        由于花不和边界抢水，所以我们可以在数组头尾设置0，表示边界，即：

        0、flowerbed[0]、flowerbed[1] 。。。 flowerbed[m]、0
        """
        flowerbed.insert(0,0)
        flowerbed.append(0) #首尾加0
        # print(flowerbed)
        count=0 #某段连续为0的数量
        for i in range(0,len(flowerbed)):
            if(flowerbed[i]==0):
                count+=1
            if(flowerbed[i]==1):
                if(count>2):
                    n-=(count-1)/2
                count=0
        if(count>2):#最后一个不是1，跳出循环判断
            n-=(count-1)/2
        if n>0:
            return False
        else:
            return True
            