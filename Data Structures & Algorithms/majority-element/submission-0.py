class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hash_table = defaultdict(int)
        res = maxCount = 0
        for i in nums:
            hash_table[i] += 1
            if maxCount < hash_table[i]: 
                res = i
                maxCount = hash_table[i]
        return res
        