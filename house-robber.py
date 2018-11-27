#coding=utf-8
"""

一个小偷要偷盗一条街道，如果连续偷盗两个相邻的房子将会报警，求在不报警的前提下能偷盗的最大价值。
经典的动态规划问题，dp[i]表示从偷到第i个房子能偷盗的最大数额（此时，i从0开始，范围内的最后一个房子可以偷也可以不偷），
最后返回dp[n-1]，dp[0]=nums[0]，dp[1]=max(nums[0],nums[1])，对于第i个屋子（此处i从0开始，这一天的价值是nums[i]），
这一天，小偷可以选择不偷盗，保持dp[i-1]，或者选择偷盗，但是偷盗的话，前一天必定不能偷盗，所以偷盗的价值是dp[i-2]+nums[i]，
所以转移方程是dp[i]=max(dp[i-1],dp[i-2]+nums[i])。

"""

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        n=len(nums)
        if n<2:
            return nums[0]
        dp=[0]*n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[n-1]
    
if __name__ == "__main__":
    print Solution().rob([8,4,8,5,9,6,5,4,4,10])