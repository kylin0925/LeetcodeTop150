class Solution {
public:
    int hIndex(vector<int>& citations) {
        int n = citations.size();
        int hidx = 0;
        //cout << n << endl;
        sort(citations.begin(), citations.end());
        for(int i = 0;i<n;i++){
            //cout <<citations[i] + i -1 << endl;
            if(citations[i] > 0) {
                if(citations[i] + i -1 < n && citations[citations[i] + i -1] >= citations[i])
                    hidx = citations[i];
                else
                    hidx = max(hidx, n-i);
            }
        }
        return hidx;
    }
};