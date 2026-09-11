class Solution {
public:
    int totalNumbers(vector<int>& digits) {
        int count[10] = {0};
        for (int d : digits) {
            count[d]++;
        }
        
        int ans = 0;
        for (int num = 100; num <= 998; num += 2) {
            int c[10] = {0};
            int temp = num;
            c[temp % 10]++;
            temp /= 10;
            c[temp % 10]++;
            temp /= 10;
            c[temp]++;
            
            bool possible = true;
            for (int i = 0; i < 10; i++) {
                if (c[i] > count[i]) {
                    possible = false;
                    break;
                }
            }
            if (possible) {
                ans++;
            }
        }
        return ans;
    }
};