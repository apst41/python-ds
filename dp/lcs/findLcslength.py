from collections import defaultdict


class Solution:
    def __init__(self):
        self.memo = defaultdict(int)
    
    def lengthOfLongestSubstring(self, f: str, s: str) -> int:
        return self.helper(f, s, len(f), len(s))
    
    def helper(self, f: str, s: str, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if f[m - 1] == s[n - 1]:
            return 1 + self.helper(f, s, m - 1, n - 1)
        
        else:
            return max(self.helper(f, s, m - 1, n), self.helper(f, s, m, n - 1))
    
    def lengthOfLongestSubstringMemo(self, f: str, s: str):
        return self.helperMemo(f, s, len(f), len(s))
    
    def helperMemo(self, f: str, s: str, m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        
        key = (m, n)
        
        if key in self.memo:
            return self.memo[key]
        
        if f[m - 1] == s[n - 1]:
            ans = 1 + self.helperMemo(f, s, m - 1, n - 1)
        
        else:
            ans = max(self.helperMemo(f, s, m - 1, n), self.helperMemo(f, s, m, n - 1))
        
        self.memo[key] = ans
        return ans
    
    def lengthOfLongestSubstringTopDown(self, f: str, s: str):
        m = len(f) + 1
        n = len(s) + 1
        dp = [[0 for _ in range(n)] for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif f[i - 1] == s[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return dp[m - 1][n - 1]


if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring('ajay', 'aajbbbbbby'))
    
    print(Solution().lengthOfLongestSubstringMemo('ajay', 'aajbbbbbby'))
    print(Solution().lengthOfLongestSubstringTopDown('a', 'aajbbbbbby'))
