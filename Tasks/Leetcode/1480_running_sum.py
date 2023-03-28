# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
# Return the running sum of nums.
# Example:
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
from typing import List


class Solution:
    @staticmethod
    def runningSum(nums: List[int]) -> List[int]:
        new_list = [sum(nums[:i+1]) for i in range(len(nums))]
        return new_list


if __name__ == "__main__":
    s = Solution
    print(s.runningSum([1, 2, 3, 4]))
