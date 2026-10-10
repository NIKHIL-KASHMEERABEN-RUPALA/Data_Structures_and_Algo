
class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        k = k1 + k2
        
        freq = Counter(abs(a - b) for a, b in zip(nums1, nums2))
        freq.pop(0, None)         
        if not freq:
            return 0
        
        heap = [(-d, c) for d, c in freq.items()]
        heapq.heapify(heap)
        
        while k > 0 and heap:
            neg_d, cnt = heapq.heappop(heap)
            d = -neg_d
            next_d = -heap[0][0] if heap else 0
            
            cost = cnt * (d - next_d)
            
            if cost <= k:
                k -= cost
                if next_d > 0:
                    if heap and -heap[0][0] == next_d:
                        neg_next, cnt_next = heapq.heappop(heap)
                        heapq.heappush(heap, (-next_d, cnt_next + cnt))
                    else:
                        heapq.heappush(heap, (-next_d, cnt))
            else:
                q, r = divmod(k, cnt)
                new_d = d - q
                if new_d > 0:
                    heapq.heappush(heap, (-new_d, cnt - r))
                if new_d - 1 > 0 and r > 0:
                    heapq.heappush(heap, (-(new_d - 1), r))
                break
        
        ans = 0
        for neg_d, cnt in heap:
            d = -neg_d
            ans += cnt * d * d
        return ans