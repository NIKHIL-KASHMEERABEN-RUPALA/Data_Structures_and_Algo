class Solution {
public:
    int numberOfSets(int n, int k) {
        long long MOD = 1e9 + 7;
        int totalPoints = n + k - 1;
        int r = 2 * k;
        
        // We need to compute C(totalPoints, r) % MOD efficiently
        if (r > totalPoints) return 0;
        if (r > totalPoints / r) r = totalPoints - r; // Optimization for symmetry
        
        vector<long long> dp(r + 1, 0);
        dp[0] = 1;
        
        for (int i = 1; i <= totalPoints; ++i) {
            for (int j = min(i, r); j > 0; --j) {
                dp[j] = (dp[j] + dp[j - 1]) % MOD;
            }
        }
        
        return dp[r];
    }
};