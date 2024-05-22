from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        m = len(grid)
        n = len(grid[0])
        
        ans = [[1000 for _ in range(n)] for _ in range(m)]
        
        def helper(x, y, i, seen):
            if x in range(m) and y in range(n) and grid[x][y] == 1 and (x, y) not in seen:
                seen.add((x, y))
                ans[x][y] = min(i + 1, ans[x][y])
                helper(x - 1, y, i + 1, seen)
                helper(x + 1, y, i + 1, seen)
                helper(x, y - 1, i + 1, seen)
                helper(x, y + 1, i + 1, seen)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    helper(i - 1, j, 0, set())
                    helper(i + 1, j, 0, set())
                    helper(i, j - 1, 0, set())
                    helper(i, j + 1, 0, set())
        
        maximum = -1
        for i in range(m):
            for j in range(n):
                print(i,j)
                # if ans[i][j] != 1000:
                #     maximum = max(maximum, ans[i][j])
        
        return maximum


if __name__ == '__main__':
    sol = Solution()
    grid = [[0,2]]
    print(sol.orangesRotting(grid))
