from typing import List

from queuepractise.testmyqueue import combinationSum


class Solution:
    
    def __init__(self):
        self.answer = None
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.answer = []
        myList = []
        candidates.sort()
        self.helper(candidates, target, 0, myList, 0)
        return self.answer
    
    def helper(self, candidates, target, currentSum, currentList, index):
        if currentSum > target:
            return
        
        if currentSum == target:
            self.answer.append(currentList)  # Append a copy of currentList
            return
        
        for i in range(index, len(candidates)):
            currentList.append(candidates[i])
            self.helper(candidates, target, currentSum + candidates[i], currentList, i)
            currentList.pop()


if __name__ == '__name__':
    
    input = [2, 3, 4, 5]
    combinationSum(input, 10)
    
