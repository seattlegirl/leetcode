#coding=utf-8
"""
统计所有小于非负整数 n 的质数的数量。

示例:

输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。

埃氏筛法步骤编辑
（1）先把1删除（现今数学界1既不是质数也不是合数）

（2）读取队列中当前最小的数2，然后把2的倍数删去
（3）读取队列中当前最小的数3，然后把3的倍数删去
（4）读取队列中当前最小的数5，然后把5的倍数删去
（5）读取队列中当前最小的数7，然后把7的倍数删去
（6）如上所述直到需求的范围内所有的数均删除或读取
注：此处的队列并非数据结构队列，如需保留运算结果，处于存储空间的充分利用以及大量删除操作的实施，建议采用链表的数据结构。
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        primes=[True]*n
        primes[0]=primes[1]=False
        for i in range(2,int(n**0.5)+1):
            if primes[i]:
                primes[i*i:n:i]=[False]*len(primes[i*i:n:i])
        return sum(primes)

if __name__ == "__main__":
    print Solution().countPrimes(10)
