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
    
    def totalPalindrom(self, s):
        ans = 0
        
        start = 0
        end = 1
        
        for i in range(len(s)):
            low = i
            high = i + 1
            
            while low >= 0 and high < len(s) and s[low] == s[high]:
                condition = high - low + 1
                if condition > end:
                    start = low
                    end = high - low + 1
                    ans += 1
                low -= 1
                high += 1
            
            low = i
            high = i
            
            while low >= 0 and high < len(s) and s[low] == s[high]:
                condition = high - low + 1
                if condition > end:
                    start = low
                    end = high - low + 1
                    ans += 1
                low -= 1
                high += 1
        return s[start:end]
    
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
    print(s.totalPalindrom("ajay"))
