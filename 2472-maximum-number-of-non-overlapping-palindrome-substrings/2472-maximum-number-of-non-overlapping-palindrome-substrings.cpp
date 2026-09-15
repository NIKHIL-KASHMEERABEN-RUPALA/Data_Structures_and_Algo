class Solution {
public:
    int maxPalindromes(string s, int k) {
        ios_base::sync_with_stdio(false);
        cin.tie(NULL);

        int n = s.length();
        vector<int> dp(n + 1, 0);

        // Helper function with boundary safety checks
        auto isPalindrome = [&](int l, int r) {
            if (l < 0) return false;
            while (l < r) {
                if (s[l++] != s[r--]) return false;
            }
            return true;
        };

        for (int i = k; i <= n; ++i) {
            dp[i] = dp[i - 1];

            // Check for palindrome of length k ending at i - 1
            if (isPalindrome(i - k, i - 1)) {
                dp[i] = max(dp[i], dp[i - k] + 1);
            }

            // Check for palindrome of length k + 1 ending at i - 1
            if (isPalindrome(i - k - 1, i - 1)) {
                dp[i] = max(dp[i], dp[i - (k + 1)] + 1);
            }
        }

        return dp[n];
    }
};