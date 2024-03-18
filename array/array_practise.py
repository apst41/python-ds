from collections import deque, OrderedDict

from list import List


def threeSum(nums):
    my_len = len(nums) - 1
    
    nums.sort()
    print(nums)
    my_set = set()
    ans = []
    
    for low in range(0, my_len):
        mid = low + 1
        high = my_len
        while mid < high:
            current = nums[low] + nums[mid] + nums[high]
            
            if current == 0:
                my_set.add(tuple([nums[low], nums[mid], nums[high]]))
            
            if current < 0:
                mid += 1
            
            else:
                high -= 1
    
    for values in my_set:
        ans.append([element for element in values])
    
    return ans


if __name__ == '__main__':
    
    my_list = threeSum([-1, 0, 1, 2, -1, -4, -2, -3, 3, 0, 4])
    my_list.sort()
    print(my_list)
