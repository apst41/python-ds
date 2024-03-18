class Solution(object):
    
    def __init__(self):
        self.maximum = 0
    
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
    
    def palindromeStringLength(self, s):
        for i in range(len(s)):
            for j in range(len(s) - 1, i - 1, -1):
                string = s[i:j]
                if self.isPalindrome(string):
                    print(string, end=' ')
    
   
    
    def isPalindrome(self, s):
        low = 0
        high = len(s) - 1
        while low < high:
            if s[low] != s[high]:
                return False
            low += 1
            high -= 1
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.palindromeStringLength('ajay'))
