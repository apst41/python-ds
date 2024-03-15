def threeSum(nums):
    my_len = len(nums) - 1
    nums.sort()
    ans = []
    
    for low in range(0, my_len):
        if low > 0 and nums[low] == nums[low - 1]:
            continue
        mid = low + 1
        high = my_len
        while mid < high:
            current = nums[low] + nums[mid] + nums[high]
            
            if current == 0:
                ans.append([nums[low], nums[mid], nums[high]])
                while mid < high and nums[high] == nums[high - 1]:
                    high -= 1
                while mid < high and nums[mid] == nums[mid + 1]:
                    mid += 1
                mid += 1
                high -= 1
            
            elif current < 0:
                mid = mid + 1
            
            else:
                high = high - 1
    
    return ans


if __name__ == '__main__':
    my_list = threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4])
    my_list.sort()
    print(my_list)
