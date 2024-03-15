import math
from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    answer = []
    myList = []
    candidates.sort()
    helper(candidates, target, 0, myList, 0, answer)
    return answer


def helper(candidates, target, currentSum, currentList, index, answer):
    if currentSum > target:
        return
    
    if currentSum == target:
        answer.append(currentList[:])
        return
    
    for i in range(index, len(candidates)):
        currentList.append(candidates[i])
        helper(candidates, target, currentSum + candidates[i], currentList, i, answer)
        currentList.pop()


if __name__ == '__main__':
    a = 2
    b = 3
    c = 2.9
    print(math.ceil(c))
