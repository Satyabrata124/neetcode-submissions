class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        k ={}

        for ind, val in enumerate(nums):
            rest= target - val

            if rest in k:
                return [k[rest],ind]
            else:
                k[val]=ind
        return []
        