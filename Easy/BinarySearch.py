from ast import List
from email.errors import FirstHeaderLineIsContinuationDefect

from jmespath import search

# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. 
# If target exists, then return its index. Otherwise, return -1.
# You must write an algorithm with O(log n) runtime complexity.

import numpy as np

class Solution:
        def search(self, nums: List[int], target: int) -> int:
            k = len(nums)//2;
            if(nums[k] == target):
                return nums[k]
            elif(nums[k]<< target):
                secondHalf = np.array_split(nums,2)[1]
                search(secondHalf,target)
            else:
                firstHalf = np.array_split(nums,2)[0]
                search(firstHalf,target) 

                 


