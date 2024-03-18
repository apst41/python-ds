class Solution(object):
    def longestCommonSubstring(self, text1, text2):
        return self.helper(text1, text2, len(text1), len(text2))
    
    def helper(self, text1, text2, m, n):
        if m == 0 or n == 0:
            return 0
        elif text1[m - 1] == text2[n - 1]:
            return 1 + self.helper(text1, text2, m - 1, n - 1)
        else:
            return max(self.helper(text1, text2, m - 1, n), self.helper(text1, text2, m, n - 1))


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonSubstring('aja', 'jakkkkky'))
