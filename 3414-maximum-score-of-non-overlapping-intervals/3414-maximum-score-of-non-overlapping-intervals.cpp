#include <vector>
#include <tuple>
#include <algorithm>

class Solution {
public:
    std::vector<int> maximumWeight(std::vector<std::vector<int>>& input) {
        int n = input.size();
        // Store intervals as tuple: {left, right, weight, original_index}
        std::vector<std::tuple<int, int, long long, int>> intervals(n);
        for (int i = 0; i < n; ++i) {
            intervals[i] = {input[i][0], input[i][1], input[i][2], i};
        }

        // Sort intervals by their starting points
        std::sort(intervals.begin(), intervals.end());

        // Precompute next non-overlapping interval index for each interval using binary search
        std::vector<int> nextIdx(n);
        for (int i = 0; i < n; ++i) {
            int l = i + 1, r = n, target = std::get<1>(intervals[i]);
            int idx = n;
            while (l < r) {
                int mid = l + (r - l) / 2;
                if (std::get<0>(intervals[mid]) > target) {
                    idx = mid;
                    r = mid;
                } else {
                    l = mid + 1;
                }
            }
            nextIdx[i] = idx;
        }

        // DP State: dp[i][k] stores {max_weight, vector_of_indices}
        // Since k is at most 4, we use fixed size small structures for efficiency.
        struct State {
            long long weight = 0;
            std::vector<int> indices;
            
            bool operator<(const State& other) const {
                if (weight != other.weight) return weight < other.weight;
                return indices > other.indices; // We want lexicographically smaller indices, so reverse for max
            }
        };

        // dp[i][k]
        std::vector<std::vector<State>> dp(n + 1, std::vector<State>(5));

        for (int i = n - 1; i >= 0; --i) {
            for (int k = 1; k <= 4; ++k) {
                // Option 1: Skip current interval
                State skip = dp[i + 1][k];

                // Option 2: Take current interval
                long long w = std::get<2>(intervals[i]);
                int orig_idx = std::get<3>(intervals[i]);
                int nxt = nextIdx[i];
                
                State pick;
                pick.weight = w + dp[nxt][k - 1].weight;
                
                // Construct the combined index list and maintain sorted order for lexicographical comparison
                pick.indices = dp[nxt][k - 1].indices;
                pick.indices.push_back(orig_idx);
                std::sort(pick.indices.begin(), pick.indices.end());

                // Choose the best state (maximum weight, or tie-break with lexicographically smaller indices)
                if (skip < pick) {
                    dp[i][k] = pick;
                } else {
                    dp[i][k] = skip;
                }
            }
        }

        // Find the best result across all valid counts (up to 4 intervals)
        State best;
        for (int k = 1; k <= 4; ++k) {
            if (best < dp[0][k]) {
                best = dp[0][k];
            }
        }

        return best.indices;
    }
};