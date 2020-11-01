# https://leetcode.com/problems/two-sum/submissions/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[num] = i
        return []
