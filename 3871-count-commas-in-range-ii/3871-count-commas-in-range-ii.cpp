class Solution {
public:
    long long countCommas(long long n) {
        long long ans = 0;
        long long threshold = 1000LL;

        while (n >= threshold) {
            ans += (n - threshold + 1);
            // Avoid overflow when multiplying by 1000
            if (threshold > LLONG_MAX / 1000) break;
            threshold *= 1000LL;
        }

        return ans;
    }
};