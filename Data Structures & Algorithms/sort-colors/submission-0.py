class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        L, i = 0, 0
        R = len(nums) - 1

        def swap(i, j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
        while i <= R:
            if nums[i] == 0:
                swap(i, L)
                L += 1
            elif nums[i] == 2:
                swap(i, R)
                R -= 1
                i -= 1
            i += 1
