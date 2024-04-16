from typing import List


class Solution:
    def rob_func(self, nums_: List[int]):
        size = len(nums_)
        if size==0:
            return 0
        if size == 1:
            return nums_[0]
        if size == 2:
            return max(nums_[0],nums_[1])
        dp = [0]*size
        dp[0] = nums_[0]
        dp[1] = max(nums_[0],nums_[1])
        for i in range(2,size):
            #dp[i-1]表示第i个house不选，
            dp[i] = max(dp[i-1],dp[i-2]+nums_[i])
        return dp[size-1]

    def rob(self, nums: List[int]) -> int:

        nums1 = nums[:-1]
        nums2 = nums[1:]

        res1 = self.rob_func(nums1)
        res2 = self.rob_func(nums2)

        return max(res1,res2)
    
sl= Solution()
nums = [1,2,3,1]
(sl.rob(nums))