def helper(nums, k, low, high):
    if low > high: return -1
    mid = low + (high - low) // 2
    
    if nums[mid] == k:
        return mid
    
    if nums[mid] > k:
        return helper(nums, k, low, mid - 1)
    else:
        return helper(nums, k, mid + 1, high)


def binary_search(nums, k):
    return helper(nums, k, 0, len(nums) - 1)


def binary_search_rotated(nums):
    low = 0
    high = len(nums) - 1
    
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > nums[high]:
            low = mid + 1
        else:
            high = mid
    return nums[low]


if __name__ == '__main__':
    print(binary_search_rotated([1, 1, 1, 4, 5]))
