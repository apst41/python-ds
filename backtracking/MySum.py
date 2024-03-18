def findTotalWays(arr, target, n):
    if target == 0 and n == 0:
        return 1
    if n <= 0:
        return 0
    
    return findTotalWays(arr, target - arr[n - 1], n - 1) + findTotalWays(arr, target, n - 1)


def topDown(arr, target):
    m = target + 1
    n = len(arr) + 1
    memo = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(m):
        memo[i][0] = 1
    
    for i in range(1, m):
        for j in range(1, n):
            if arr[i - 1] <= j:
                memo[i][j] = memo[i - 1][j - arr[i - 1]] + memo[i - 1][j]
            
            else:
                memo[i][j] = memo[i - 1][j]
        
        return memo[m - 1][n - 1]
    
    # Driver Program


if __name__ == "__main__":
    arr = [1, 1, 1, 1, 1]
    
    # print(topDown(arr, 3))
    
    # target number
    target = 3
    print(topDown(arr, target))

# print(findTotalWays(arr, 3, len(arr)))
