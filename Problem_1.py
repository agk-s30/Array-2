# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

# Time complexity: O(n) 
# Space complexity: O(1)
# Explanation: Traverse the array and mark the index -1 of the array as negative; then traverse again and return the indices + 1 of the positive numbers

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []

        for i in range(len(nums)):
            j = abs(nums[i]) - 1
            nums[j] = abs(nums[j]) * -1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        
        return res
