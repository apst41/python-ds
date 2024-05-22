from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        
        current = 1
        ans = 1
        
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                current += 1
            elif nums[i] == nums[i + 1]:
                continue
            else:
                ans = max(current, ans)
                current = 1
        
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]))
