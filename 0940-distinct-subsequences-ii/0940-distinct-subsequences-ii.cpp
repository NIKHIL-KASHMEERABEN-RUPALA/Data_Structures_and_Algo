class Solution {
public:
    int distinctSubseqII(string s) {
        // Fast I/O for competitive programming environments
        ios_base::sync_with_stdio(false);
        cin.tie(nullptr);

        constexpr int MOD = 1'000'000'007;
        
        // last_added[c] stores the count of new distinct subsequences
        // created when character c was last processed.
        int last_added[26] = {0};
        int total = 0; // Total distinct non-empty subsequences so far

        for (unsigned char ch : s) {
            int idx = ch - 'a';
            
            // New subsequences formed by appending `ch`:
            // Append `ch` to all existing distinct subsequences (+ total)
            // Plus `ch` by itself as a single-character subsequence (+ 1)
            // Minus duplicates from previous occurrences of `ch` (- last_added[idx])
            long long new_subseqs = (1LL + total - last_added[idx]) % MOD;
            if (new_subseqs < 0) {
                new_subseqs += MOD;
            }

            // Update total distinct subsequences
            total = (total + new_subseqs) % MOD;
            
            // Update the records for character `ch`
            last_added[idx] = (last_added[idx] + new_subseqs) % MOD;
        }

        return total;
    }
};