class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int minBuy = prices[0];
        int maxProfit = 0;
        int minIdx = 0;
        for(int i = 1 ; i < prices.size() ; i++) {
            if(prices[i] - prices[minIdx] > maxProfit) {
                maxProfit = prices[i] - prices[minIdx];
            }
            if(prices[i] < prices[minIdx]) {
                minIdx = i;
            }
        }
        return maxProfit;
    }
};