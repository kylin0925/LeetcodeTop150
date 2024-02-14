class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int maxProfit = 0;
        int minIdx = 0; 
        for(int i = 1; i < prices.size(); i++) {
            int tmp = prices[i] - prices[minIdx];
            if(tmp > 0) {
                maxProfit += tmp;
                minIdx = i;
            }else{
                if(prices[minIdx] > prices[i])
                    minIdx = i;
            }
        }
        return maxProfit;
    }
};