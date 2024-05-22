import collections
from typing import List


class mySum(object):
    
    def __init__(self):
        self.hash = collections.defaultdict()
    
    def topDown(self, nums, target):
        m = len(nums) + 1
        n = target + 1
        
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        dp[0][0] = 1
        
        for i in range(1, m):
            for j in range(0, n):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[m - 1][n - 1]
    
    def subset_sum(self, a: list, n: int, sum: int):
        
        # Initializing the matrix
        tab = [[0] * (sum + 1) for i in range(n + 1)]
        tab[0][0] = 1
        for i in range(1, sum + 1):
            tab[0][i] = 0
        
        for i in range(1, n + 1):
            for j in range(sum + 1):
                if a[i - 1] <= j:
                    tab[i][j] = tab[i - 1][j] + tab[i - 1][j - a[i - 1]]
                else:
                    tab[i][j] = tab[i - 1][j]
        return tab[n][sum]
    
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        array_sum = sum(nums)
        
        if array_sum < target:
            return 0
        if target == 0 and array_sum != 0:
            return 0
        
        new_target = (target + array_sum) // 2
        
        return max(self.helper(nums, new_target, len(nums)), self.helper(nums[::-1], new_target, len(nums)))
    
    def helperForMinDiff(self, nums: List[int], target: int) -> int:
        m = len(nums) + 1
        n = target + 1
        
        dp = [[0 for j in range(n)] for i in range(m)]
        
        dp[0][0] = 1
        
        for i in range(1, m):
            for j in range(0, n):
                if nums[i - 1] <= j:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        mn = float('inf')
        end = (n - 1) // 2
        for j in range(0, end):
            mn = min(mn, target - 2 * j)
        return mn
    
    def targetSum(self, nums, target):
        return max(self.helper(nums, target, len(nums)), self.helper(nums[::-1], target, len(nums)))
    
    def helper(self, nums, target, n):
        if n == 0:
            if target == 0:
                return 1
            else:
                return 0
        
        key = (target, n)
        
        if key in self.hash:
            return self.hash[key]
        
        if nums[n - 1] <= target:
            ans = self.helper(nums, target - nums[n - 1], n - 1) + self.helper(nums, target, n - 1)
        else:
            ans = self.helper(nums, target, n - 1)
        
        self.hash[key] = ans
        return ans
    
    def findmaxSum(self, nums):
        maxSum = nums[0]
        for i in range(1, len(nums)):
            maxSum = max(maxSum, maxSum + nums[i], nums[i])
        return maxSum


if __name__ == '__main__':
    nums = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    
    nums1 = [-36,36]
    
    print(mySum().findmaxSum(nums1))
    # print(mySum().topDown([1, 1, 1, 1, 1], 4))
    # print(mySum().findTargetSumWays([1, 1, 1, 1, 1], 3))
    # print(mySum().findTargetSumWays([7, 9, 3, 8, 0, 2, 4, 8, 3, 9], 0))
    print(mySum().subset_sum(nums, len(nums), 0))
    print(mySum().topDown(nums, 0))
    print(mySum().targetSum(nums, 0))
    #print(mySum().helperForMinDiff(nums1, sum(nums1)))
