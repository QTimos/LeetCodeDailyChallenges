from typing import List
class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        num_of_subarrays = 0
        i = 0
        while i < len(nums):
            num = nums[i]
            j = i
            target_count = 0
            while j < len(nums):
                if j < len(nums) and nums[j] == target:
                    target_count += 1
                if target_count >  (j - i + 1) // 2:
                    num_of_subarrays += 1
                j += 1
            i += 1
        return num_of_subarrays


def main() -> None:
    s = Solution()
    nums = [1, 1, 1, 1]
    target = 1
    print(s.countMajoritySubarrays(nums, target))


if __name__ == "__main__":
    main()
