from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash = defaultdict()
        
        for i in range(0, len(nums)):
            
            sum = target - nums[i]
            
            if sum in hash:
                return [i, hash[sum]]
            else:
                nums[i] = i
        
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))
