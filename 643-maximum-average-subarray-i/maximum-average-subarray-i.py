class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        i = 1
        result = sum(nums[:k]) / k
        a = sum(nums[i:k])
        for j in range(k, len(nums)):
            a += nums[j]
            if a / k > result:
                result = a / k
            a -= nums[i]
            i += 1
        return result