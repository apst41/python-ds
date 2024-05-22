from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        
        minjumps = 9999999999999
        
        inf = 9999999999999999
        
        def helper(i):
            
            global minjumps
            if i == len(nums) - 1:
                return 0
            
            if nums[i] == 0:
                return inf
            
            for i in range(i + 1, len(nums)):
                jumps = helper(i)
                
                if 1 + jumps < inf:
                    minjumps = min(1 + jumps, minjumps)
            return minjumps
        
        return helper(0)
