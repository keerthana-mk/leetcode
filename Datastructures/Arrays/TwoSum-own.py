# Input: nums = [3,2,4], target = 6
# Output: [1,2]

class Solution:
    def twoSum_own(self, nums: list[int], target: int) -> list[int]:
        dict ={}
        for i in range(len(nums)):
            if target - nums[i] in dict:
                # dict[target-nums[i]] = i
                return [dict[target-nums[i]],i]
            else:
                dict[nums[i]] =i

s = Solution()
nums = [3,2,4]
target = 6
print(s.twoSum_own(nums,target))