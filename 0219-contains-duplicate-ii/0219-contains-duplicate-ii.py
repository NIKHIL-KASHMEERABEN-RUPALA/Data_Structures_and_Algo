class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_seen = {}

        for index , val in enumerate(nums):
            if val in last_seen and abs(index-last_seen[val]) <= k:
                return True

            last_seen[val] = index

        return False