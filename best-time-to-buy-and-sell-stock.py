#coding=utf-8
"""
给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。

如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

注意你不能在买入股票前卖出股票。

示例 1:

输入: [7,1,5,3,6,4]
输出: 5
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
示例 2:

输入: [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。

维持两个变量，最低买入价格和当前可达到的最高利润，从第二天开始遍历，小于最低价格那么我们更新最低价格变量，
然后以这一天的价格作为卖出价格，那么利润就是卖出价格-最低价格，最次也就是0，也就是我更新了最低价格还以最低价格卖出去了，
因为不能用之前的价格卖，此时利润也要相应的更新，大于保存的最大利润我们就更新，遍历完成后得到结果。

"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)<=1:
            return 0
        buy_price=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            buy_price=min(buy_price,prices[i])
            max_profit=max(max_profit,prices[i]-buy_price)
        return max_profit

if __name__ == "__main__":
    print Solution().maxProfit([7,1,5,3,6,4])