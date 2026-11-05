class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        ans = 0

        for x in arr1:
            i = bisect_left(arr2, x)

            if (i == len(arr2) or arr2[i] - x > d) and \
               (i == 0 or x - arr2[i - 1] > d):
                ans += 1

        return ans