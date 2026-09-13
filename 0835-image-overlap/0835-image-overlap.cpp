class Solution {
public:
    int largestOverlap(vector<vector<int>>& img1, vector<vector<int>>& img2) {
        int n = img1.size();
        vector<pair<int, int>> ones1, ones2;
        
        // Collect coordinates of all 1s in both images
        for (int i = 0; i < n; ++i) {
            for (int j = 0; j < n; ++j) {
                if (img1[i][j] == 1) ones1.push_back({i, j});
                if (img2[i][j] == 1) ones2.push_back({i, j});
            }
        }
        
        // Fixed-size frequency array to store translation offsets.
        // Size 100x100 is more than enough for n <= 30.
        // We add +n to handle negative coordinate differences safely.
        int count[100][100] = {0};
        int maxOverlap = 0;
        
        // Count frequencies of each translation vector
        for (const auto& p1 : ones1) {
            for (const auto& p2 : ones2) {
                int dx = p2.first - p1.first + n;
                int dy = p2.second - p1.second + n;
                
                count[dx][dy]++;
                maxOverlap = max(maxOverlap, count[dx][dy]);
            }
        }
        
        return maxOverlap;
    }
};