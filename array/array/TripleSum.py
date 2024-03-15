
def triple_sum(inputArray,targetSum):
    inputArray.sort()

    for low in range(len(inputArray)):
         high = len(inputArray)-1
         mid = low+1
         while mid < high:

              sum = inputArray[low] + inputArray[mid] + inputArray[high]

              if sum == targetSum:
                   print(sum)
                   print(inputArray[low], inputArray[mid], inputArray[high])
                   break

              elif sum > targetSum:
                   high -= 1

              elif sum < targetSum:
                   mid = mid + 1



if __name__=='__main__':

      triple_sum([10,2,3,4,5,6,7,8,9,1],10)