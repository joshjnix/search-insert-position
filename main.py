class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        correct = 0
        for i in range(len(nums)):
            if nums[i] == target:
                return nums.index(target)
                correct += 1
                break
        if correct != 1:
            nums.append(target)
            nums.sort()
            return nums.index(target)
