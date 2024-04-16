from typing import List

# class Solution:
    # def rob(self, nums: List[int]) -> int:
        
    #     if not nums:
    #         return 0
    #     size=len(nums)

    #     if size==1:
    #         return nums[0]
    #     elif size==2:
    #         return max(nums[0],nums[1])

    #     dp =[0]*size
    #     dp[0] = nums[0]
    #     dp[1] = max(nums[0],nums[1])

    #     for i in range(2,size):
    #         #$偷窃第 k间房屋，那么就不能偷窃第 k−1间房屋，偷窃总金额为前k−2间房屋的最高总金额与第 k间房屋的金额之和。不偷窃第 k间房屋，偷窃总金额为前 k−1 间房屋的最高总金额。
    #         dp[i]=max(dp[i-2]+nums[i],dp[i-1])
    #     return dp[size-1]
nums =[183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
class Solution:
    # 朴素dfs
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # 返回第i个房屋及之后能偷窃到的最大值，issteal标志第i - 1个房屋是否偷窃
        def dfs(i, issteal):
            # i越界，没房屋可供偷窃，只能空手而归了>_<
            if i >= n:
                return 0
            # 前一个偷过了，那这个就不能偷了！去下一家看看~
            elif issteal:
                return dfs(i + 1, False)
            # 前一个没偷过，那么这个可偷可不偷，两者取大的那个
            else:
                return max(dfs(i + 1, True) + nums[i], dfs(i + 1, False))

        return dfs(0, False)
    
sl=Solution()
print(sl.rob(nums))