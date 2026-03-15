class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i, val in enumerate(nums):
            difference = target - val

            if difference in checked:
                return [checked[difference],i]

            checked[val] = i
        return 0