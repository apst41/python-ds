from collections import defaultdict

ans = []


def helper(nums, index, sum, currentSum, currentList):
    if currentSum > sum: return None
    if currentSum == sum:
        ans.append(currentList[:])
    
    for i in range(index, len(nums)):
        currentList.append(nums[i])
        helper(nums, i + 1, sum, currentSum + nums[i], currentList)
        currentList.pop()


def givenSumAllList(nums, sum):
    my_list = []
    helper(nums, 0, sum, 0, my_list)


if __name__ == "__main__":
    givenSumAllList([2, 3, 8, 10, 17, 12, 15, 5], 11)

    for i in ans:
    
        print(i)
    
